# import graphics
from graphics import Point, GraphWin, Circle

my_point = Point(50,70)
point_a = Point(70,90)  # values x and y are referred to as instance variables
# print(point_a.getX(), point_a.getY())  # returns x and y value and evaluates to a float
# methods are accessed through dot notation
point_a.move(10, 0)  # moves x to 80 and y remains the same
# print(point_a.getX(), point_a.getY())  # brought down to see changes can delete

win = GraphWin("CSCI 220", 700, 700)
middle = Point(350, 350)
middle.draw(win)

my_circle = Circle(middle, 70)  # circle keeps track of center as a point (x,y) and radius as a float
my_circle.draw(win)
# has default values
#point_a.draw(win)  # when you called methods you call it to object not class
input("hit enter to close")