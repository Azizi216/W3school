import time
import math
import operator
from functools import reduce
import os
import string
# os stands for operating sytem
# it gives your paython program the abilit ti interact with files, folder, and permissions on your computer
# once you do import os, you can:
# check if a file exist
# chcek who can access it(read/write/run)
# create folders, rename files, etc


# in here we get the path from the user
path = input("Enter the path to list directories and files")

print("\n Directories: ")
# list only directories
directories = [d for d in os.listdir(
    path) if os.path.isdir(os.path.join(path, d))]
print(directories)
print("\nFiles:")
files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
print(files)

list_all = os.listdir(path)
print("all files")
print(list_all)
# a directory is just another word for folder on our compter

# ok lets break down this code
# os.listdir(path) is a built-in fuction that gives you all files and folders in the folder at path
# for d in ... loop over each item (file or folder)
# os.path.join(path, d) Gets the full path of the item
# os.path.isdir(...) check if the item is a folder
# if only includ it if its a directory
# [d for ...] build a list of only the folders

# second task
# Get the path from the user
path = input("Enter the path to check for access")
if os.path.exists(path):
    print("The path exists")
    # checking if its readable
    if os.access(path, os.R_OK):
        print("The file is read able")
    else:
        print("the file is not readble")
    # checking if the path is writable
    if os.access(path, os.W_OK):
        print("the path is write able")
    else:
        print("the file is not readable")
    if os.access(path, os.X_OK):
        print("the file is execuatble")
    else:
        print("the file is not execuatble.")
else:
    print("the file does not exist")

# this code checks if a file or folder path exists, and if it does, it chceks
    # if it can be read
    # if it can be written to
    # if it can be run/ executed
# if os.path.exists(path):
# this cecks: does this file or folder actually exist?
# true if it exist
# flse if it does not
# os.access() this function checks if the file or folder has a specific type of access
# Read Access(os.R_OK)
# os.access(path, os.R_OK)
# cheks: Can I read this file
# for example can I open a .txt file to see the text inside
# can you open a folder to see its contents
# true if readable
# false if not(maybe your'not allowed)
# Write Access(os.W_OK)
# os.access(path, os.W_OK)
# checks Can i write to this file or folder
# for example can i edit and save this file
# can you create or delete files in a folder
# Execute Access(os.X_ok)
# os.access(path, os.X_OK)
# chcek "Can I run this file like a program "
# on files: used for .exe files or Python scripts
# on folders:
# Measn; Can I go inside that folder using the command line?


# TASK 3

# Getting input
all_list = ''
path = input("please insert your desired path: ")
if os.path.exists(path):
    all_list = os.path.dirname(path)
    print(all_list)
    file_name = os.path.basename(path)
    print(file_name)
else:
    print("access is not allowed")
# os.path.exists(path)
# check does this file or folder actually exist?
# os.path.exist(...) is a funtion from the os module
# it returns:
    # true is it exist
    # flase if it does'nt
# os.path.dirname(path):
# takes the full path
# just removes the file name
# Example if the full path is  "C:\\Users\\John\\Documents\\notes.txt"
# it returns "C:\\Users\\John\\Documents"
# as you see it removes the file name

# task 4
# getting the file name from the user:
file_name = input("please insert your File name: ")

try:
    # open the file in read more
    with open(file_name, "r") as file:
        # intializing the line count;
        line_count = 0
        for line in file:
            line_count += 1
    print("The total number of line is", line_count)
except FileExistsError:
    print("The file does not exist. Please check the filename and try again")
# try: ... except:
# this is a try-except block
# it is used to catch errors so your program does not crash if something goes wrong.
# if something inside the try block fails, python jumps to the except blokc and runs that code instead

# with open(file_name, "r") as file:

# this line tries to open the file in read mode("r")
# "with" is a safe way to open files. it automatically close the file after your done.
# if the file exists, it gets opened
# if does not exist, an error happens and the code jumps to the except

# for line in file this for loop says "Give me one line at a time from this file"
# python automatically reads each line for you

 # Task 5:
# simple python that writs a list to a file:
# defining the list of items
my_list = ["apple", "banana", "cherry", "Date"]
# Getting the file name from the user
file_name = input(
    "please insert the filename of ur txt file with txt extension")
# open the file in write mode
with open(file_name, "w") as file:
    for item in my_list:
        file.write(item + '\n')
print("List has been written to ", file_name)

# task 6
"""
file_name = 'A'
for i in string.ascii_uppercase:
    file_name = f"{i}.txt"  # it creats the filename
    with open(file_name, "w") as file:
        file.write(f"this is the fle for the letter {i}.")
print("26 txt files have been created")
"""

# task 7

sourcr_file = input("Enter the name of the source file(with .txt extension): ")
destination_file = input("Enter the name of the destination file (with .txt)")
try:
    # open the source file in read mode
    with open(sourcr_file, 'r') as src:
        content = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(content)
    print("Content copied successfully from",
          sourcr_file, "to", destination_file)
except FileNotFoundError:
    print("the source file does not exist. please check the filename and try again")

# task 8

# Get the file path from the user
file_path = input("Enter the path of the file to delete: ")

# Check if the file exists
if os.path.exists(file_path):
    print("The file exists.")

    # Check if the file is writable (to ensure it can be deleted)
    if os.access(file_path, os.W_OK):
        # Attempt to delete the file
        try:
            os.remove(file_path)  # Delete the file
            print("The file has been deleted successfully.")
        except Exception as e:
            print("An error occurred while trying to delete the file:", e)
    else:
        print("The file is not writable. Cannot delete the file.")
else:
    print("The file does not exist.")


# Built in function

numbers = [2, 3, 4, 5]

result = reduce(operator.mul, numbers)
print("Multiplication of all numbers:", result)

# task2: count the uppercase and lowercase letter in a string


def count_case(text):
    upper_case = sum(1 for c in text if c.isupper())
    lower_case = sum(1 for c in text if c.islower())
    print("Uppercase letters:", upper_case)
    print("Lowercase letters:", lower_case)


# Example:
count_case("Hello World!")

# task 3


def is_palindrome(s):
    return s == s[::-1]


# Example:
string = "madam"
if is_palindrome(string):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
# invoke square root after specific Milisecond


def delayed_sqrt(num, delay_ms):
    time.sleep(delay_ms / 1000)  # convert ms to seconds
    result = math.sqrt(num)
    print(f"Square root of {num} after {delay_ms} milliseconds is {result}")


# Example:
delayed_sqrt(25100, 2123)

# retun true if all the elment of the tuple are true
t = (True, 1, "hello", 3.14)

print("All elements are true:", all(t))
