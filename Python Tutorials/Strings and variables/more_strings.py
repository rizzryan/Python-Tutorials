# This is a continuation of user_input.py. The only difference is that this is a bit more complex :)

# Pay attention and figure out what makes this more complicated than user_input.py

x = raw_input('Enter in a number here: ')
y = raw_input('Enter in another number here: ')

print int(x) + int(y)

print x + y

# Notice how in line 8, you are able to correctly add the two numbers together. 

# You are abe to add in line 8 only because x and y have been casted as integers.

# Line 10 is only print x and y conjoined as a string because x and y were not casted in that case.