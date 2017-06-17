# So far, we have learned about how to sotre user inout into variables, print statements, and how to do some basic math.

# Here, we will go over some more complex math and cover casting a bit more since a number can be either an integer or float, which is a decimal.

# The basic math operation signs are +, -, /, and *. 

# + stands for addition. You will use this operation to sum two or more numbers together.

# - stands for subtraction. You will use this operation to find the difference of two or more numbers. 

# / stands for division. You will use this operation to find the quotient of numbers.

# * stands for multiplication. You will use this operation to multiply numbers together to get the product. 

number1 = raw_input('Enter in a number for your first number: ')
number2 = raw_input('Enter in a number for your second number: ')

print int(number1) + int(number2)

print int(number1) - int(number2)

print int(number1) * int(number2)

print int(number1) / int(number2)

# Notice how when you divide by the number, you may not get the most exact, decimal form of the quotient.

# This is because the number was casted as an integer instead of a decimal. Lets try it with a decimal.

# Line 24 will round the quotient to the nearest whole number.

print float(number1) / int(number2)

print float(number1) / float(number2)

print int(number1) / float(number2)

# As long as one of the number in the division operation is a float, or decimal, you will get a more exact answer in the form of a decimal.