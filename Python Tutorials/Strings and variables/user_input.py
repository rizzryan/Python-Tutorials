# In this example, you will be able to learn how to store user input into a variable and then print out the string stored in the variable.

# Variables are used to store information such as your name, age, etc. You can make variables hold any kind of information.

# Declaring a variable is very simple, look at the example on line 7.

age = raw_input('What is your age? ')
name = raw_input('What is your name? ')

# Pay attention to the syntax of getting user input

# This prints out what you stored in the variables age and name

print 'Hello, ' + name + '. You are ' + str(age) + ' years old.'

# You may ask what is str() in line 14. This casts, or in other words transforms the variable that is not a string into a str. 