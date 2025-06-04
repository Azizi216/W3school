# there are two boolean value in python 1. true and 2.false
# when you campare two value the you use from camparators
print(10 > 9)
print(10 == 9)
print(10 < 9)

# print a message based ina a if statemnet, python returns True or False
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# the bool() function allows you to evalaute any value, and give you True or False in return
print(bool("Hello"))
print(bool(15))

# evalute two values
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

# Most Values are True
# almost any value is evaluated to True if it has some sort of content
# any string is True, except empty string
# any number is true, except 0
# any list, tuple, set, and dictionary are True, except empty ones
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# the followingj will return false
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

# functions can create a function that returns a Boolean Value


def myFunction():
    return True


print(myFunction())

# print yes if the funtion returns True, otherwise print 'no'


def myFunction():
    return True


if myFunction():
    print("YES!")
else:
    print("NO!")

# isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x, int))

# python operators

# paython operatros are used to perform operations on variable and values
print(10 + 5)

"""""Python divides the operators in the following groups:

Arithmetic operators
Assignment operators
Comparison operators
Logical operators
Identity operators
Membership operators
Bitwise operato """

"""""Python Arithmetic Operators
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator	Name	Example	Try it
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y """

"""Python Assignment Operators
Assignment operators are used to assign values to variables:

Operator	Example	Same As	Try it
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)"""

"""Python Comparison Operators
Comparison operators are used to compare two values:

Operator	Name	Example	Try it
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y"""
"""Python Identity Operators
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator	Description	Example	Try it
is 	Returns True if both variables are the same object	x is y	
is not	Returns True if both variables are not the same object	x is not y	
"""
"""Python Membership Operators
Membership operators are used to test if a sequence is presented in an object:

Operator	Description	Example	Try it
in 	Returns True if a sequence with the specified value is present in the object	x in y	
not in	Returns True if a sequence with the specified value is not present in the object	x not in y """
"""Python Bitwise Operators
Bitwise operators are used to compare (binary) numbers:

Operator	Name	Description	Example	Try it
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2"""

"""The precedence order is described in the table below, starting with the highest precedence at the top:

Operator	Description	Try it
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR """

"""List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:"""

thislist = ["apple", "banana", "cherry"]
print(thislist)

# List items are ordered, changeable, and allow duplicate value
# list are changeable and allow duplicate
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# list Length can be evaluated by lne() function
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

# list item data type
# list can store string, int and boolean data type
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# a list can contain different data type
list1 = ["abc", 34, True, 40, "male"]

# data type of a list is list
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# the list constructore
# note the double round-brackets
thislist = list(("apple", "banana", "cherry"))
print(thislist)
# there are collection data type in python programming language
# list a collection which is ordered and changeable.Allow dupilicate members

# tuples is a collection which is ordered and unchangeable. Allow duplicate membres
# set is a colection which is unorderd, unchangeable and unindexed. No duplicate
# Dictionary is a collection which is ordered and changable. No duplicate

# list items are indexed and you can access them by referring to the index
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative index means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# you can specify a rnage of index by specifying where to start and wher to end

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# by leaving out the end value the range will go on to the end of the list
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# Range of Negative Index
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# change item value
# to change the value of a specific item refer to the index

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# change a range of item values

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

# if you insert more item than you replace the new item will be inserted where you specified
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

# changhe the second and third value by repalcing it with one value

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# to insert a new list item, without replacing any of the existing values, we can use the insert()
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# append item add elemnt at the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# to insert at a value at a specific index
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# to append elemnt from another list to the currnet list, use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

# add any iterable value with extend()
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

# remove specific value
# we use form remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# remove from specifeid index
# we use from pop()
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# if you do not specify the index, the pop() method removes the last item

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# the del key word also remove from list
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# the del key word can also delete the list completly
thislist = ["apple", "banana", "cherry"]
del thislist

# claer() empties the list
# the list still remains but it has no content
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# to loop throw a list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# to loop throw index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# you can loop throw a while loop we use the len()
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# looping using list comperhension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# list comperehension offers a short syntax when you want to creat a new list based on the value
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

# with lsit comperehension you can do all that in one of a code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

# the syntax the return value is a new list leaving the old list unchanged

newlist = [x for x in fruits if x != "apple"]

# you can use the range() function to create an iterable
newlist = [x for x in range(10)]
print(newlist)

# same example but with acondition
newlist = [x for x in range(10) if x < 5]
print(newlist)

# set the value in new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]

print(newlist)

# set all value to "hello" in new list
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]

print(newlist)

# return orange instead of banana
newlist = [x if x != "banana" else "orange" for x in fruits]
# sort object have a sort()  method that will sort the objects alphanumarically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# sort the list numerically
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# sort in deciding order
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)
# sort this is decindidng order
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist)
# sort based on how close the number is to 50


def myfunc(n):
    return abs(n - 50)


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# sort is case senesetive which measns first all uppper case letters sort then lower case
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)


# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

# reverse method reverse the curret sorting item
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# you can not compy a list simply by declearing a new list variable and puttin the old one inside the new one
# you can from copy built in list method copy()
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# another method way to make a copy of the list is list() method
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# you can also make a copy of the list by slice
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

# there are several ways to join or concatenate, two or more lists in python

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# you can also concatnate two list by using append()

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# you can also use from extend method to join two lidt

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# a tuple is a collection of which is ordered ans unchanged
# tuple items are ordered and is indexed

# tuple allows duplicate values
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# to determine how many items exist in tuple we use from len()
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# to creat a tuple with one item  you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thistuple = ("apple",)
print(type(thistuple))

# NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# tuple items can be any data type string, int, boolean
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# a tuple can contain different data type as well
tuple1 = ("abc", 34, True, 40, "male")

# From Python's perspective, tuples are defined as objects with the data type 'tuple':
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
# it is also possible to make a tuple by using tuple constructor
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

# access tuple item by refereing  to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# negative indexing means start from the end.
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# you can specify a range index to where you statrt
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])


# to check if a specific item exist in a tuple we use from "in" build in function thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

    # once a tuple created you cannot change its value. tuples are unchangable or immutable as it aslo is called
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add item
# since tuples are immuatable, they do  noyt have a built in append() method, but there are other ways to add items to tuples

# covert into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

# create a new tupel with value ornage and add that tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# Convert the tuple into a list, remove "apple", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# the key word will delete the tuple completly
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)  # this will raise an error because the tuple no longer exists

# when we extract the values back into variables. this is called unpacking
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# if the number of varriables is less than the number of the values, you can add * to the values will be assigned to the varriable as a list
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# a for loop is used for iterating over a sequence (that is either a list a tuple, a dictionary a set or a string)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# even strings are iterable objects, they contian a sequrnce of chraters
for x in "banana":
    print(x)

# with the break statment we can stop the loop before it has looped through all the items
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# exist the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# the continue statment
# with the cntinue statment we can stop the the current iteration of the loop, and continue with the next

# Do not print banana
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# the range() Function
# to loop through a set of code a specfied number of times we can use the range() function

for x in range(6):
    print(x)

# using the the start parameter
for x in range(2, 6):
    print(x)

# the range() function default to increment the sequence by 1
# however it is possible to specifiy the increament value by adding a third parameter range(2, 30, 3)
for x in range(2, 30, 3):
    print(x)
# the else keyword in a for loop specifies a blokc of code to be executed when the loop is finised
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# break  the loop when x is 3 and see what happens withe the else block
for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")

# Neseted loops
# the inner loop will be executed one time for each iteration of the outer loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# the pass statment for loop cannot be empty, but if you some reasons have a for
# with no content , put pass statment
for x in [0, 1, 2]:
    pass

# a function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# a function can retun data as a result

# in pyhon a function is defined using the def keyword


def my_function():
    print("Hello from a function")

# to call a function use function name followed by parenthesis


def my_function():
    print("Hello from a function")


my_function()

# Sets are used to store multiple items in a single variable.
# A set is a collection which is unordered, unchangeable*, and unindexed.
# Sets are written with curly brackets.

# Set items are unordered, unchangeable, and do not allow duplicate values.
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
# to know how many elemnets exits in a set we use from len()

thisset = {"apple", "banana", "cherry"}

print(len(thisset))

# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
# sets can store with multiple variable
set1 = {"abc", 34, True, 40, "male"}
# type of a set is set

myset = {"apple", "banana", "cherry"}
print(type(myset))

# it is also possible to make a set by set constructore
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# you can not access the element of the set by index
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)

# check if "banana" exist in the set
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)

# check if banana is not in the set
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

# for adding an item to a set we use from add()  method

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)

# to add item from another set to the currnet set

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)

# add any iterable object
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

# to remove an item in a set, use the remove(), or the discard() methid
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)

# Remove "banana" by the discard() method
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)

# Remove a random item by using the pop() method

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

# del key word delet the set completly
thisset = {"apple", "banana", "cherry"}

del thisset

print(thisset)

# you can loop thorw items
thisset = {"apple", "banana", "cherry"}

for x in thisset:
    print(x)
""" Join Sets
There are several ways to join two or more sets in Python.

The union() and update() methods joins all items from both sets.

The intersection() method keeps ONLY the duplicates.

The difference() method keeps the items from the first set that are not in the other set(s).

The symmetric_difference() method keeps all items EXCEPT the duplicates."""

# The union() method returns a new set with all items from both sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

# u can use the | operator instead of the union() method, and you will get the same result.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)

# When using a method, just add more sets in the parentheses, separated by commas:

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

# When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 | set4
print(myset)

# The union() method allows you to join a set with other data types, like lists or tuples.
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# The update() method inserts all items from one set into another.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# The intersection() method will return a new set, that only contains the items that are present in both sets.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# You can use the & operator instead of the intersection() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# Join sets that contains the values True, False, 1, and 0, and see what is considered as duplicates:
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# You can use the - operator instead of the difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the original set instead of returning a new set.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)

# Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

# dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Changeable Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
# Dupliacte not allowed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# To determine how many items a dictionary has, use the len() function:
print(len(thisdict))

# Dictionary data type can be any data type
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
# and dictionary type is dict

# it is also possible to make a dictionary by dict constructre
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")

# The keys() method will return a list of all the keys in the dictionary.
x = thisdict.keys()

# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change

# The values() method will return a list of all the values in the dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["year"] = 2020

print(x)
# after the change
# Add a new item to the original dictionary, and see that the values list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "red"

print(x)  # after the change


# Make a change in the original dictionary, and see that the items list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()

print(x)  # before the change

car["year"] = 2020

print(x)  # after the change
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change the "year" to 2018:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

# Update the "year" of the car by using the update() method:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

# Adding an item to the dictionary is done by using a new index key and assigning a value to it:

ExampleGet your own Python Server
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

# Add a color item to the dictionary by using the update() method:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"color": "red"})
# The pop() method removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict
print(thisdict)  # this will cause an error because "thisdict" no longer ex

# The clear() method empties the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# Loop Through a Dictionary

for x in thisdict:
    print(x)

for x in thisdict:
    print(thisdict[x])

for x in thisdict.values():
    print(x)

# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
    print(x)
# Loop through both keys and values, by using the items() method:

for x, y in thisdict.items():
    print(x, y)

# Make a copy of a dictionary with the copy() method:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# another way to make a copy is to use built in funtion
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Create a dictionary that contain three dictionaries:

myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:
print(myfamily["child2"]["name"])
for x, obj in myfamily.items():
    print(x)

    for y in obj:
        print(y + ':', obj[y])

"""Python Conditions and If statements
Python supports the usual logical conditions from mathematics:

Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
These conditions can be used in several ways, most commonly in "if statements" and loops.

An "if statement" is written by using the if keyword."""

# If statement:

a = 33
b = 200
if b > a:
    print("b is greater than a")

# The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".

Example
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# The else keyword catches anything which isn't caught by the preceding conditions.

Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# You can also have an else without the elif:
# Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

if a > b:
    print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

a = 33
b = 200
if not a > b:
    print("a is NOT greater than b")

x = 41

if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

a = 33
b = 200

if b > a:
    pass
# The match statement selects one of many code blocks to be executed.

SyntaxGet your own Python Server
match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block

day = 4
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

day = 4
match day:
    case 6:
        print("Today is Saturday")
    case 7:
        print("Today is Sunday")
    case _:
        print("Looking forward to the Weekend")

day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends!")

month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("No match")

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

for x in range(6):
    print(x)

for x in range(2, 6):
    print(x)

for x in range(2, 30, 3):
    print(x)


for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3:
        break
    print(x)
else:
    print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

for x in [0, 1, 2]:
    pass
