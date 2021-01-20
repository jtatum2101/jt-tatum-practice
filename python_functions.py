# Define a function which takes 2 numbers as arguments and returns the absolute
# value of the difference
def absolute_difference(num1, num2):
    return abs(num1-num2)
print(absolute_difference(3,9))


# Define a function which takes two strings, first_name and last_name, and
# returns a string like "Hello <full name>, how are you?"
def greeting (first_name, last_name):
    '''(str, str) -> str'''
    return f'Hello {first_name} {last_name}, how are you?'
print(greeting('jeremiah', 'tatum'))

# You need to implement a function which is part of a public API, it should do
# the same as above, but the arguments should be in reverse order: last_name,
# first_name. You should consider calling the function above instead of
# redefining.
def greeting_public(last_name, first_name):
    return greeting(first_name, last_name)

print(greeting_public('tatum', 'jeremiah'))


# Define a function which takes a variable number of strings and returns a
# single string which joins all the arguments with commas. Make sure to reject
# any arguments that are not strings. How should you reject? Should you ignore
# or raise an error?



            




# Define a function which takes a single string and then an optional keyword
# argument. The keyword argument should be called "capitalize" and if True is
# passed, it should return the string in all caps. Otherwise, the string that
# was originally passed should be returned unmodified.



# Define a class called Dog which implements a Dog. The dog shoud be
# initialized with a name, breed, and sex for the dog. The dog should have
# methods "bark" which takes an integer between 1 and 4 inclusive for how loud
# the dog barks. It should return a string about how loud the dog barked. The
# class should also have "walk" method which takes two tuples of integers that
# represent x, y coordinates for the start and stop. It should return a string
# which tells how far the dog walked. Lastly, the dog class should have a to
# string method which returns a string describing the dog.
