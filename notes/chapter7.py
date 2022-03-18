import math
# relational operators
# less than <
# less than or equal to <=
# greater than >
# greater than or equal to >=
# equality ==
# not equal !=

# bool stands for boolean
# possible values for booleans are true or false / T and F are reserved values in python
# conditions return True or False / based on that it decides whether to run body


# def convert():
#     celsius = eval(input("What is the temperature in celsius? "))
#     fahrenheit = celsius * (9 / 5) + 32
#     print("The temperature is", fahrenheit, "degrees fahrenheit.")
#     if fahrenheit > 90:
#         print("Woah that's hot!")
#     if fahrenheit > 90 and fahrenheit < 30:
#         print("It feels great out!")
#     if fahrenheit < 30:
#         print("Brrr that's cold!")
#


# def quadratic(a, b, c):
#     disc = b * b - 4 * a * c
#     if disc < 0:
#         print('no real roots')  # these are considered MUTUALLY EXCLUSIVE OUTCOMES
#     elif disc == 0:
#         sqrt_discr = math.sqrt(disc)
#         denom = 2 * a
#         root_1 = (-b + sqrt_discr) / denom
#         print("double root at:", root_1)
#     else:
#         sqrt_discr = math.sqrt(disc)
#         denom = 2 * a
#         root_1 = (-b + sqrt_discr) / denom
#         root_2 = (-b - sqrt_discr) / denom
#         print("root 1:", root_1, "root 2:", root_2)
#
#
# if __name__ == '__main__':
#     # convert()
#     quadratic(1, 1, 2)

# and operator takes bool on right and bool on left returns a bool
# and requires both p and q are to be true to evaluate as true otherwise it will be false
# for example
# x = 9
# if x > 3 and x < 10:
#     print("True")

# how to find the maximum of three values
# def maximum(a, b, c) one way to do it but is clunky and not efficient
#     if a >= b and a >= c:
#         return a
#     if b >= a and b >= c:
#         return b
#     return c

# def maximum (a, b, c): another way but not best
#     if a >= b:
#         if a >= c:
#             return a
#         else:
#             return c
#         if b >= c:
#             return b
#         return c
#
#
# maximum()


# def maximum (a, b, c): better way to go about it
#     max_value = a
#     if b > max_value:
#         max_value = b
#     if c > max_value:
#         max_value = c
#     if a > max_value:
#         max_value = a
#     return max_value
#
#
# maximum(3, 2, 1)

def maximum(values): # how to find a maximum of a list
    max_value = values[0]
    for value in values:
        if value >= max_value:
            max_value = value
    return max_value

maximum([-1, -7. -3. -2. -4])

# Errors are exceptions and are "thrown"
# Errors have types and are objects
# try: allows you to attempt to run something even though there might be an error
# example
# try:
#     blah
#     blah
#     blah
# except SyntaxError as e:
#     print("blahblah")
#     print(e) # this will print the error