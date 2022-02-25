from graphics import *


def target():
    win = GraphWin("Circle", 700, 700)
    center = Point(350, 350)
    radius = 250
    circle = Circle(center, radius)
    circle.draw(win)
    circle.setFill("yellow")

    circle2 = Circle(center, 225)
    circle2.draw(win)
    circle2.setFill("red")

    circle3 = Circle(center, 200)
    circle3.draw(win)
    circle3.setFill("blue")

    circle3 = Circle(center, 175)
    circle3.draw(win)
    circle3.setFill("black")

    circle4 = Circle(center, 150)
    circle4.draw(win)
    circle4.setFill("white")

    message2 = Text(Point(350, 650), "Click to end the program")
    message2.draw(win)

    win.getMouse()
    win.close()
