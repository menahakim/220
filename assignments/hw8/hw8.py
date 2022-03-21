"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""

import math
from graphics import GraphWin, Point, Circle, Text


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    acc = 0
    for i in range(len(nums)): # must return integers not lists
        acc = nums[i] + acc
    return acc



def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = eval(nums[i])


def sum_of_squares(nums):
    listofsums = []
    for i in range(len(nums)):
        nums[i] = nums[i].split(",")
        to_numbers(nums[i])
        square_each(nums[i])
        listofsums.append(sum_list(nums[i]))  # sum list is a function nums i is the list of squared values
    return listofsums  # here we create a new list so you must return it


def starter(weight, wins):
    if weight >= 150 and weight < 160 and wins >= 5:
        return True
    elif weight > 199 or wins > 20:
        return True
    else:
        return False


def leap_year(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 == 0) and (year % 100 != 0):
        return True
    else:
        return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_point = win.getMouse()
    distance = math.sqrt(
        (center.getX() - circumference_point.getX()) ** 2 + (center.getY() - circumference_point.getY()) ** 2)
    circle_one = Circle(center, distance)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center2 = win.getMouse()
    circumference_point2 = win.getMouse()
    distance2 = math.sqrt(
        (center2.getX() - circumference_point2.getX()) ** 2 + (center2.getY() - circumference_point2.getY()) ** 2)
    circle_two = Circle(center2, distance2)
    circle_two.setFill("light pink")
    circle_two.draw(win)
    overlaps = did_overlap(circle_one, circle_two)
    if overlaps == True:
        Text(Point(350, 500), "The circles overlap!")
    else:
        Text(Point(350,500), "The circles do not overlap!")
    win.getMouse()


def did_overlap(circle_one, circle_two):
    xdistance = (circle_two.getCenter().getX() - circle_one.getCenter().getX())
    ydistance = (circle_two.getCenter().getY() - circle_one.getCenter().getY())
    sum = math.sqrt((xdistance)**2 + (ydistance)**2)
    getradius = circle_one.getRadius() + circle_two.getRadius()
    if getradius >= sum:
        return True
    else:
        return False





if __name__ == '__main__':
    numbers = [10, 20, 30, 40, 50]
    add_ten(numbers)
    print(numbers)
    square_each(numbers)
    print(numbers)
    sum_is = sum_list(numbers)  # each functions overrides previous one
    print(sum_is)
    stringlist = ["10", "20", "30", "40", "50"]
    to_numbers(stringlist)
    add_ten(stringlist)
    print(stringlist)
    sumofsquarelist = ["3,7.2,9", "12,15,20"]
    sumofsquaresum = sum_of_squares(sumofsquarelist)
    print(sumofsquaresum)





