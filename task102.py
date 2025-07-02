import pygame
import sys
import random
import sqlite3

# === Database Setup ===
conn = sqlite3.connect("snake_game.db")
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS user (
    username TEXT PRIMARY KEY
)
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS user_score (
    username TEXT,
    level INTEGER,
    score INTEGER,
    FOREIGN KEY (username) REFERENCES user(username)
)
""")
conn.commit()

# === User Input ===
username = input("Enter your username: ")

cur.execute("SELECT * FROM user WHERE username=?", (username,))
user = cur.fetchone()
if not user:
    cur.execute("INSERT INTO user(username) VALUES(?)", (username,))
    conn.commit()
    level = 1
    score = 0
else:
    cur.execute(
        "SELECT level, score FROM user_score WHERE username=?", (username,))
    data = cur.fetchone()
    if data:
        level, score = data
    else:
        level, score = 1, 0

print(f"Welcome, {username}! Starting at level {level} with score {score}")

# === Pygame Setup ===
pygame.init()
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 35)

# === Level Settings ===
levels = {
    1: {'speed': 10, 'walls': []},
    2: {'speed': 15, 'walls': [(200, 200, 200, 20), (100, 100, 20, 200)]},
    3: {'speed': 20, 'walls': [(150, 150, 300, 20), (150, 230, 20, 120)]}
}

# === Snake & Food ===
snake = [(100, 50), (80, 50), (60, 50)]
direction = (CELL_SIZE, 0)
food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
        random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)

paused = False


def draw_walls(walls):
    for wall in walls:
        pygame.draw.rect(screen, (255, 0, 0), wall)


def save_progress():
    cur.execute("DELETE FROM user_score WHERE username=?", (username,))
    cur.execute("INSERT INTO user_score(username, level, score) VALUES (?, ?, ?)",
                (username, level, score))
    conn.commit()


def game_over():
    global running
    save_progress()
    print("Game Over! Your score:", score)
    pygame.quit()
    sys.exit()


# === Game Loop ===
running = True
while running:
    clock.tick(levels[level]['speed'])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused
                if paused:
                    save_progress()
            elif event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    if paused:
        continue

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + direction[0], head_y + direction[1])
    snake.insert(0, new_head)

    # Check collisions
    if (new_head[0] < 0 or new_head[0] >= WIDTH or
        new_head[1] < 0 or new_head[1] >= HEIGHT or
            new_head in snake[1:]):
        game_over()

    for wall in levels[level]['walls']:
        if pygame.Rect(wall).collidepoint(new_head):
            game_over()

    if new_head == food:
        score += 10
        if score >= level * 50 and level < len(levels):
            level += 1
        food = (random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
                random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE)
    else:
        snake.pop()

    # Draw
    screen.fill((0, 0, 0))
    draw_walls(levels[level]['walls'])
    for block in snake:
        pygame.draw.rect(screen, (0, 255, 0), (*block, CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, (255, 255, 0), (*food, CELL_SIZE, CELL_SIZE))
    score_text = font.render(
        f"User: {username}  Level: {level}  Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()

# === Save before exit ===
save_progress()
pygame.quit()
conn.close()
