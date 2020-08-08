# Unit 1 - everythin is an object
#
# In python, all data is objects !!!
# This includes all numbers (int and float types), strings, functions etc.
# If you still don't know about all these (i.e: you are new to programming), don't worry !!!
# You will learn about them later.

# The lines are called "assignments".
# They create new objects, and make new name reference the new objects.

# For example: the name dave_age references a new object of the type int
dave_age = 34

# So objects have types, but names do not have types. Names just reference objects.
# If you're coming from other programming languages, you know all about variables.
# There are really no "variables" in python. In the rare occasion where someonw write that word, what they
# really mean is: a name that references some object.


#Let's define some more:
marbles_count = 100

# We can check the type of the object referenced by a name:
print('Dave age is:', dave_age)
print('You have', marbles_count, 'marbles.')


# The type built-in function gets a reference to an object.
# It returns the type of the object being referenced
# again, there is no type to a name in Python
print(type(dave_age))
print(type(marbles_count))

# If you use your interpreter interactively, you don't need to use print(...)
# So.,try to type this:
type(dave_age)
type(marbles_count)

# You can learn more about the print and type functions in python here:
#  https://docs.python.org/3/library/functions.html#type
#  https://docs.python.org/3/library/functions.html#print