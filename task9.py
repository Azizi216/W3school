import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Racer Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Font
font = pygame.font.SysFont("Arial", 20)

# Player settings
player = pygame.Rect(175, 500, 50, 70)
player_speed = 5

# Enemy settings
enemy = pygame.Rect(random.randint(0, 350), 0, 50, 70)
enemy_speed = 3

# Coin settings
coins = []
coin_timer = 0
coin_spawn_delay = 30  # frames
coin_weights = [1, 2, 3]

# Scoring
score = 0
total_collected = 0
increase_every_n = 5  # Increase enemy speed every 5 coins collected

# Game loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < WIDTH:
        player.x += player_speed

    # Enemy movement
    enemy.y += enemy_speed
    if enemy.top > HEIGHT:
        enemy.x = random.randint(0, WIDTH - enemy.width)
        enemy.y = 0

    # Coin spawning
    coin_timer += 1
    if coin_timer >= coin_spawn_delay:
        coin_timer = 0
        coin_x = random.randint(0, WIDTH - 20)
        coin = {
            "rect": pygame.Rect(coin_x, 0, 20, 20),
            "value": random.choice(coin_weights)
        }
        coins.append(coin)

    # Coin movement and collision
    for coin in coins[:]:
        coin["rect"].y += 3
        if coin["rect"].colliderect(player):
            score += coin["value"]
            total_collected += 1
            if total_collected % increase_every_n == 0:
                enemy_speed += 1
            coins.remove(coin)
        elif coin["rect"].top > HEIGHT:
            coins.remove(coin)

    # Drawing
    pygame.draw.rect(screen, GREEN, player)
    pygame.draw.rect(screen, RED, enemy)

    for coin in coins:
        pygame.draw.circle(screen, YELLOW, coin["rect"].center, 10)

    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    if player.colliderect(enemy):
        game_over_text = font.render("Game Over!", True, WHITE)
        screen.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()

pygame.quit()
sys.exit()



# Game state

# snake


import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

clock = pygame.time.Clock()
FPS = 10

# Snake initial settings
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)  # moving right initially

# Food settings
foods = []  # list of foods on the board
food_weights = [1, 2, 3]  # different weights
food_lifetime = 50  # lifetime in frames

# Score
score = 0
font = pygame.font.SysFont("Arial", 20)

def spawn_food():
    x = random.randint(0, (WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    y = random.randint(0, (HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
    weight = random.choice(food_weights)
    foods.append({"pos": (x, y), "weight": weight, "timer": food_lifetime})

# Spawn first food
spawn_food()

running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)

    # Move snake
    head_x, head_y = snake[0]
    new_head = (head_x + snake_dir[0], head_y + snake_dir[1])
    snake.insert(0, new_head)

    # Check wall collision
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Check self collision
    if new_head in snake[1:]:
        print("Game Over")
        pygame.quit()
        sys.exit()

    # Check if snake eats food
    eaten = False
    for food in foods[:]:
        if new_head == food["pos"]:
            score += food["weight"]
            foods.remove(food)
            spawn_food()
            eaten = True
            break

    if not eaten:
        snake.pop()  # only grow if food eaten

    # Update and draw foods
    for food in foods[:]:
        # Draw food with color based on weight (optional)
        color = YELLOW
        if food["weight"] == 2:
            color = (255, 165, 0)  # orange
        elif food["weight"] == 3:
            color = RED

        pygame.draw.rect(screen, color, (*food["pos"], CELL_SIZE, CELL_SIZE))
        food["timer"] -= 1
        if food["timer"] <= 0:
            foods.remove(food)
            spawn_food()

    # Draw snake
    for part in snake:
        pygame.draw.rect(screen, GREEN, (*part, CELL_SIZE, CELL_SIZE))

    # Show score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
sys.exit()

# paint

# Initialize Pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint App")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (100, 100, 255)

# Font
font = pygame.font.SysFont("Arial", 20)

# Clock
clock = pygame.time.Clock()

# Drawing state
drawing = False
start_pos = None
shape = "square"  # default shape

# Function to draw a square


def draw_square(surface, start, end):
    size = max(abs(end[0] - start[0]), abs(end[1] - start[1]))
    rect = pygame.Rect(start[0], start[1], size, size)
    rect.normalize()
    pygame.draw.rect(surface, BLUE, rect, 2)

# Function to draw right triangle


def draw_right_triangle(surface, start, end):
    points = [start, (start[0], end[1]), end]
    pygame.draw.polygon(surface, BLUE, points, 2)

# Function to draw equilateral triangle


def draw_equilateral_triangle(surface, start, end):
    x1, y1 = start
    x2, y2 = end
    size = math.dist(start, end)
    point1 = (x1, y1)
    point2 = (x2, y2)
    # Find 3rd point using rotation
    angle = math.radians(60)
    dx, dy = x2 - x1, y2 - y1
    x3 = x1 + dx * math.cos(angle) - dy * math.sin(angle)
    y3 = y1 + dx * math.sin(angle) + dy * math.c
