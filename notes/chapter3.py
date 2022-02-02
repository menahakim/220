# Data Types

# "Hello, World!" - String

# 3 - Integer = Whole number

# 3.0 Floating points type Not same as Whole number Not as accurate

# 1/3 0.33

# % or mod is useful for repeating or finding if a number is even or odd

# Math operators + - * (** exponent) / // %

# sqrt(9) - To find square root

import math # imports math files from python

sqrt = math.sqrt(9)
print(sqrt)

power = math.pow(2,3) # or 2 ** 3 What is in parentheses are called parameters ex. math.pow requires 2 number values
print(power)          # parameters are always seperated by commas

print(math.pi)

my_range = range(10)
my_range = range(3,10) # numbers have to be integers
my_range = range(3,10,2)
my_range = range (10,3, -1)
print(list(my_range)) # one parameter is when to stop, two parameters shows start and end, three parameters shows start, step

# start default = 0
# step default = 1
# if you want to count down must put negative in the step


# accumulator pattern

my_sum = 0
for i in range(101):
    my_sum = my_sum + i
    print(my_sum)

# factorial
# Analysis restate problem = Find the factorial of a given number
# Specify - inout - the number, output the factorial result, multiply and loop
# Design - Get user input for number, Initialize accumulator (fact), Loop through range (based on user input),
# Test fact = fact * i
# Maintain - Print fact

user_input = eval(input("Enter value to find factorial:"))
factorial = 1
for i in range(user_input, 0, -1):
    factorial = factorial * i
    print(factorial)

# calculate roots of a quadratic

# Analysis restate problem = Find the roots of a quadratic function
# Specify - inputs a, b, c outputs root 1, root 2
# Design - Ask user to input a, b, c
# Test fact = Solve for positive case (root 1) first then solve for negative case (root 2)
# Maintain - Print the roots

a, b, c = eval(input("Enter coefficients a, b, c:"))
sqrt_discr = math.sqrt(b * b-4 * a * c)
den = 2 * a
root 1 = (-b + sqrt_discr ) / den
root 2 = (-b - sqrt_discr) / den
print("root 1:", root_1, "root 2:", root_2)




