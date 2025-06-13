import re


def match_a_followed_by_b(s):
    pattern = r"a(b*)"
    return re.fullmatch(pattern, s) is not None


# Example usage
print(match_a_followed_by_b("a"))        # True
print(match_a_followed_by_b("ab"))       # True
print(match_a_followed_by_b("abb"))      # True
print(match_a_followed_by_b("ac"))       # False

# Match a string that has an 'a' followed by two to three 'b's


def match_a_followed_by_two_to_three_b(s):
    pattern = r"ab{2,3}"
    return re.fullmatch(pattern, s) is not None


# Example usage
print(match_a_followed_by_two_to_three_b("abb"))   # True
print(match_a_followed_by_two_to_three_b("abbb"))  # True
print(match_a_followed_by_two_to_three_b("abbbb"))  # False

# Find sequences of lowercase letters joined with an underscore


def find_lowercase_with_underscore(s):
    pattern = r"[a-z]+(_[a-z]+)+"
    return re.findall(pattern, s)


# Example usage
# ['hello_world', 'world_this', 'this_is']
print(find_lowercase_with_underscore("hello_world_this_is_python"))

# Find sequnces of uppercase letter followed by lowercase letters


def find_uppercase_followed_by_lowercase(s):
    pattern = r"[A-Z][a-z]+"
    return re.findall(pattern, s)


# Example usage
print(find_uppercase_followed_by_lowercase(
    "Hello World"))  # 3['Hello', 'World']

# Match a string that has an 'a' followed by anything ending in 'b'


def match_a_followed_by_anything_ending_in_b(s):
    pattern = r"a.*b$"
    return re.fullmatch(pattern, s) is not None


# Example usage
print(match_a_followed_by_anything_ending_in_b(
    "a quick brown fox jumps over the lazy dog b"))  # True
print(match_a_followed_by_anything_ending_in_b("a quick brown fox"))  # False

# Replace all occurrences of space, comma, or dot with a colon


def replace_with_colon(s):
    return re.sub(r"[ ,\.]", ":", s)


# Example usage
# Hello:world:How:are:you?
print(replace_with_colon("Hello, world. How are you?"))

# convert a snake case string to camel case string


def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])


# Example usage
print(snake_to_camel("hello_world"))  # helloWorld

# split a string at uppercase lettres


def split_at_uppercase(s):
    return re.findall(r'[A-Z][^A-Z]*', s)


# Example usage
# ['Hello', 'World', 'This', 'Is', 'Python']
print(split_at_uppercase("HelloWorldThisIsPython"))

# insert spaces between words starting with a caoital letters


def insert_spaces_between_capitals(s):
    return re.sub(r'(?<!^)(?=[A-Z])', ' ', s)


# Example usage
# Hello World This Is Python
print(insert_spaces_between_capitals("HelloWorldThisIsPython"))

# convert a given camel case string to snake case


def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()


# Example usage
print(camel_to_snake("HelloWorld"))  # hello_world
