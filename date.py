from datetime import datetime, timedelta
import math

x = datetime.now()
print(x)
# this is made a current date time with imorting the library datetime
new_date = x - timedelta(days=5)
print(new_date)

# timedelta create a duration of five days
# now we created a date time that is five days before

# creating a programm that prints yesterday today and tomarrow
yesterday = datetime.now() - timedelta(days=1)
print(yesterday)
today = datetime.now()
print(today)
tomarrow = datetime.now() + timedelta(days=1)
print(tomarrow)
yesterday = yesterday.replace(microsecond=0)
print(yesterday)

# this program print yesterday, today, and tomarrow
# by uisng timedelta

# writing a programm that drop the microsecond from programm
yesterday = yesterday.replace(microsecond=0)
print(yesterday)
# in this programm we created a program that replace the microsecond with 0
date1 = datetime(2025, 6, 1, 12, 0, 0)  # june 1, 2025, 12:00
date2 = datetime(2025, 6, 12, 15, 30, 0)  # june 12, 2025, 15:30:00
date_difference = date1 - date2
print(date_difference)
# jsut created a programm that find the date difference of two days

# chaging the degree to radiont

number = float(input("please insert a number? "))
new = number*(math.pi/180)
print(new)

# writing a programm th calcualte the area of trapeziod
base1 = float(input("please insert the base 1: "))
base2 = float(input("please insert the base 2: "))
h = float(input("please insert the hight? "))
area = ((base1+base2)*h)/2
print(area)

# writing a programm that caculate the area of regular polygon
n = float(input("please insert the number of sides of polygon? "))
s = float(input("please insert the length of one side? "))
p = float(input("please insert the area of polygon? "))
area = 1/4 * n * (s ** 2) * (1/math.tan(math.pi/n))
print(area)

len = int(input("please insert lenght of base: "))
hight = int(input("please insert the hight of the parallegram: "))
area = len * hight
print(area)

# Generators generate the element you loop over
# and are functions like iterators
# "Generates" the element in a loop

# you can loop over objects in memory by using generators
# a function is used yield instead of return is called generator


class student:
   # def __init__(self):
    # self.a = 1

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        val = self.a
        self.a += 2
        return val


val = student()
print(next(val))
print(next(val))

# Generator to yield squares of numbers up to N


def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i

# Function to print even numbers between 0 and n in comma-separated form


def print_even_numbers(n):
    even_numbers = (i for i in range(n + 1) if i % 2 == 0)
    print(', '.join(map(str, even_numbers)))

# Generator to yield numbers divisible by 3 and 4 between 0 and n


def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

# Generator to yield squares of numbers from a to b


def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

# Generator to yield numbers from n down to 0


def countdown(n):
    for i in range(n, -1, -1):
        yield i


# Testing the generators
if __name__ == "__main__":
    # Input for even numbers
    n = int(input("Enter a number n to print even numbers between 0 and n: "))
    print_even_numbers(n)

    # Input for divisible by 3 and 4
    n = int(
        input("Enter a number n to find numbers divisible by 3 and 4 between 0 and n: "))
    print("Numbers divisible by 3 and 4:", list(divisible_by_3_and_4(n)))

    # Input for squares from a to b
    a = int(input("Enter the starting number a for squares: "))
    b = int(input("Enter the ending number b for squares: "))
    print("Squares from a to b:")
    for square in squares(a, b):
        print(square)

    # Input for countdown
    n = int(input("Enter a number n for countdown: "))
    print("Countdown from n to 0:")
    for number in countdown(n):
        print(number)
