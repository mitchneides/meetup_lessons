# Python is a general-purpose interpreted, interactive, object-oriented, and high-level programming language.
# It was created by Guido van Rossum during 1985- 1990.

# Python was designed for readability, & has some similarities to the English language with influence from mathematics.
# Python uses new lines to complete a command, as opposed to other programming languages which often use
# semicolons or parentheses.

# Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes.
# Other programming languages often use curly-brackets for this purpose.

# Online compiler:
# repl.it
# https://www.onlinegdb.com/online_python_compiler



# Basic Value types:

# STRINGS are chains of characters we use to represent text.

first_string = "hello world"
second_string = 'hello world'

# String functions:
# We can manipulate strings using built-in functions.

'hello'.capitalize()
'hello'.upper()
'HELLO'.lower()
'goodnight moon'.replace('goodnight', 'hello')


# NUMBERS:
# There are two types of numbers in Python: Integers and Floats. Integers are whole numbers such as 1, 14 and so on.
# Floats are decimal numbers such as 3.6, 103.98…

# Operations
# You can perform all sorts of mathematical operations using numbers: addition, subtraction, division, multiplication…

ex_1 = 3 + 18
ex_2 = 66 - 18
ex_3 = 3 * 9
ex_4 = 12 / 5
ex_5 = 6 % 4


# TYPE CASTING:
# In Python '12' is not the same as 12. The first is a string and the second is an integer.

# You can transform the string '12' into an integer through a process called type casting:

test = '12' * 2
test_2 = int('12') * 2
test_3 = str(30)


# You can add a string with a string, and a number with a number, but not a number with a string.
"Hello" + "World"
"Hello "*4
"Hello" + " " + "World"
("Hello" + "World" + " ")*2

# Trying to add a string with a number will throw an error:
"My favorite number is " + 8


# BOOLEANS
# Booleans are binary operators, they are either True or False.
# They let you define an action based on the “truthiness” or “falseness” of a given statement.
# We tend to use them with comparison operators such as greater than, lower than, equal to

3 > 4
4 >= 4
3 < 4

'hello' == 'hello'
'hello' != 'hello'

# You can combine operators to test for multiple conditions
True and False
# False

3 < 4 and 2 > 1
# True

'b' == 'a' and 'c' == 'c'
# False

True or False
# True

3 < 4 or 2 > 1
# True

'b' == 'a' or 'c' == 'c'
# True



# VARIABLES
# Variables are used to store temporary pieces of data.
# A variable is like a little box in which we can store anything (string, integer…).
#
# Every variable has a name and a value, the value can be any data type.
# We can use the content of our box to perform operations on the data that was stored.
#
# Why should we use variables ?
# Variables are here to make your code dynamic
# When programming, you want to be able to run the same piece of code but with different values

my_hair_color = "black"
print(my_hair_color)

my_number = 5
my_number += 4
print(my_number)


# Taking user input
# The input function lets us ask the user for their own input. This function always gives you a string in return.

number = input('Multiply me by three: ')
print(number * 3)

print(int(number) * 3)


# CONDITIONALS
# Conditional statements are an universal programming paradigm to take certain actions based on data comparison.
# It’s our way of communicating to the computer,
# if something is true then perform such action, otherwise perform an other action.

# IF STATEMENTS
# The basic keyword to create a condition is if followed by the condition we want to implement and a colon.
# After that comes the block of code to execute if the condition is True.

a = 33
b = 200
if a > b:
    print("a is greater than b")

print("Finished")


# The elif keyword is pythons way of saying “if the previous conditions were not true, then try this condition”.
a = 33
b = 200

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")

print("Finished")

# The else keyword catches anything which isn’t caught by the preceding conditions.
# If our condition results to False then we can set a default behavior to revert to using else.
# The block of code that follows will execute every time the if block goes to False.
a = 33
b = 200

if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
else:
    print("b is greater than a")

print("Finished")


# in keyword can be used to check if a value is in a sequence.
8 in [1,2,3,4,5]
# False

"A" in "ABCD"
# True

# LISTS
# Lists let you store a collection of items.
# These items can be of any type: integers, strings, booleans or even other lists.

my_hobbies = ["Eat", "Sleep", "Code"]
my_hobbies[0]
my_hobbies[1]
my_hobbies[2]
my_hobbies[-1]

# List is mutable, it means the content can be changed.
# To change an element in a list, refer to the index number and assign a new value.

my_hobbies[1] = "Meditate"
# ["Eat", "Meditate", "Code"]


# Adding an element to a list is called appending.
my_hobbies.append("Baseball")
# ["Eat", "Meditate", "Code", "Baseball"]


# There are several methods to remove items from a list.

# To remove a specified item, use the remove method, this method removes the first occurence of the element.
my_hobbies.remove("Meditate")
# ["Eat", "Code", "Baseball"]

# To remove an item by its index, use the pop method, this method removes the element at the given index and returns it.
my_hobbies.pop(0)
# ["Code", "Baseball"]

# Adding two lists will concatenate them.
my_hobbies = ["Food", "Code"]
additional_hobbies = ["Sport", "More code"]

my_hobbies + additional_hobbies
# ["Food", "Code", "Sport", "More code"]


# len() function allows to retrieve the number of items contained in a given list.
len(my_hobbies)

numbers = [3, 12, 1, -4]
sum(numbers)
# 12

numbers = [3, 5, 1, 2]
sorted(numbers)
# [1, 2, 3, 5]

# More info:

# Sets are another sequence type, it’s unordered, it means it does not support indexing, and it doesn’t support duplicate too.
# We basically use it to make some list with no duplicates in it
my_set = set()
my_set.add("Rick")
my_set.add("Morty")
my_set.add("Rick")
print(my_set)
# {"Rick", "Morty"}

# Tuples are immutable lists, it means items can’t be changed.
# To create a tuple, use parentheses:
my_tuple = (5,6,7)


# LOOPS
# Loops are a basic programming concept that allow you to iterate over the items of a list or repeat a given action
#  a defined or even infinite number of times.

# When used in conjunction with lists, loops let you access each element successively of said list.
# We call this process “iterating”.

# In computer programming, a loop is a sequence of instructions that is continually repeated
# until a certain condition is reached.

# There are two main types of loops: for loops and while loops.
fruits = ['apple', 'banana', 'kiwi', 'pear']

for fruit in fruits:
  print(fruit)


# apple
# banana
# kiwi
# pear


# While loops differ from for loops in that they have what we call an indefinite iteration cycle.
# What that means is that the number of times they execute isn’t defined by the length of a given list
# but by a specific break point that will stop the loop’s execution when it is hit.

# A while loop is defined somewhat similarly to a conditional statement.
# The loop will keep running as long as the set condition is True and
# stop the instant that this condition evaluates to False.
# It will execute all the instructions in the loop, then test the condition,
# if the condition is still true, it will execute the loop again, and again, until the condition become false.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 1
# 2
# 3
# 4
# 5


password = ''
while password != 'hello-world-123':
  password = input('What is the top secret password? ')

print('You guessed the right password!')

# Some conditions will always be True, for example, if we run this code:
while 1 == 1:
    print("Looping...")

# It will never stop, because 1 is always equal to 1. We can also use while 1: or while True:.
