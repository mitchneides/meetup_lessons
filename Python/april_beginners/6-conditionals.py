# CONDITIONALS
# Conditional statements are an universal programming paradigm to take certain actions based on data comparison.
# It's our way of communicating to the computer,
# if something is true then perform such action, otherwise perform an other action.
# IF STATEMENTS
# The basic keyword to create a condition is if followed by the condition we want to implement and a colon.
# After that comes the block of code to execute if the condition is True.
a = 33
b = 200
if a > b:
    print("a is greater than b")
    
print("Finished")
# The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
a = 33
b = 200
if a > b:
    print("a is greater than b")
elif a == b:
    print("a is equal to b")
print("Finished")
# The else keyword catches anything which isn't caught by the preceding conditions.
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
