"""
Name: <Mena Hakim>
<ProgramName>.py

Problem: Completing arithmetic problems in python.

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math

def sum_of_threes():
    upper = eval(input("Enter the upper bound"))
    step1 = upper/3
    print(step1)


def multiplication_table():
    my_range = (1, 10, +1)
    print(my_range)

def triangle_area():
    sidea = eval(input("Enter the length of side a"))
    sideb = eval(input("Enter the length of side b"))
    sidec = eval(input("Enter the length of side c"))
    step1 = (sidea + sideb + sidec) / 2
    step2 = step1*(step1 - sidea)*(step1-sideb)*(step1-sidec)
    squareofarea = math.sqrt(step2)
    print(squareofarea)


def sum_squares():
    my_sum = 0
    lower = eval(input("Enter lower number"))
    upper = eval(input("Enter upper number"))
    mylist = []
    for i in range(lower, upper+1):
        squaresum = i * i
        mylist.append(squaresum)
    for i in mylist:
        my_sum = my_sum + i
    print(my_sum)


def power():
    result = 1
    base = eval(input("Enter the base:"))
    exponent = eval(input("Enter the exponent:"))
    for i in range(exponent):
        result = base * result
    print(str(base) + " " + "^" + " " + str(exponent) + " " + "=" + " " + str(result))



if __name__ == '__main__':
    pass
