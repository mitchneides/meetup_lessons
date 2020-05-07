# LOOPS
# Loops are a basic programming concept that allow you to iterate over the items of a list or repeat a given action
#  a defined or even infinite number of times.
# When used in conjunction with lists, loops let you access each element successively of said list.
# We call this process "iterating".
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
# What that means is that the number of times they execute isn't defined by the length of a given list
# but by a specific break point that will stop the loop's execution when it is hit.
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
