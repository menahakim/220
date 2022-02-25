# Functions are used to reduce code
import math
from graphics import *
math.sqrt(9)


# def happy(holiday):
#     print("Happy {} dear {}!" .format(holiday, name))
#
#
# def sing(name, holiday):  # these are called parameters
#     happy(holiday)
#     happy(holiday)
#     print("Happy {} Birthday dear {}!".format(holiday,  name))
#     happy(holiday)


# sing("Josef", "Sweet Sixteen")  # these are called arguments
# print()  # Creating the sing function allows us to avoid code duplicates
# sing("Emily", "Valentine's Day")


#  scope of a variable is when and where it is accessible to the program
#  anything indented within a function is the function body or the name variable for example
#  The scope of these is limited to the function sing

# def square(num):
#     x = num * num
#     return x
#
#
# number = square(10)
# print(number)

def distance(p1, p2):
    x1 = p1.getX()
    y1 = p1.getY()
    x2 = p2.getX()
    y2 = p2.getY()
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))


my_distance = distance(Point(2, 3), Point(3, 4))
print(my_distance)

# sum_diff(num_1: num_2: int) -> sum: int, diff: int

def sum_diff(x, y):
    return x + y, x - y


my_sum, my_diff = sum_diff(10, 7)
print(my_sum, my_diff)


def get_discount(price, sale):  # 100 .20 -> will return 80
    price = price * (1 - sale)
    print(price)


price = 100
get_discount(price, .20)
print(price)


def change_point(p, x, y):
    p.move(x, y)


my_point = Point(2, 3)  # any complex data type changes
change_point(my_point, 100, 200)
print(my_point.getX(), my_point.getY())