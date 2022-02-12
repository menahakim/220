
"""
Name: <Mena Hakim>
<ProgramName>.py

Problem: <Learning to use graphing functions>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: <Sam Austin>
"""

import math
from graphics import GraphWin, Circle, Point, Text, Rectangle

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", 400, 400)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(50, 50), (Point(100, 100)))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for _ in range(num_clicks):
        click = win.getMouse()
        center = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        change_x = click.getX() - center.getX()
        change_y = click.getY() - center.getY()
        shape = Rectangle(Point(click.getX() - 25, click.getY() - 25), (Point(click.getX() + 25, click.getY() + 25)))
        shape.draw(win)
        shape.setOutline("red")
        shape.setFill("red")
    instructions.setText("Click again to close")

    win.getMouse()
    win.close()


#squares()

def rectangle():

    win = GraphWin("Rectangle", 700, 700)
    corner1 = win.getMouse()
    corner2 = win.getMouse()
    shape = Rectangle(corner1, corner2)
    shape.draw(win)
    height = abs((corner2.getX() - corner1.getX()) * 2)
    length = abs((corner2.getY() - corner1.getY()) * 2)
    perimeter = height + length
    area = (height / 2) * (length / 2)
    message1 = Text(Point(600, 650), "Perimeter:\n"+str(perimeter))
    message2 = Text(Point(650, 650), "Area:\n"+str(area))
    message3 = Text(Point(350, 650), "Click to end the program")
    message1.draw(win)
    message2.draw(win)
    message3.draw(win)

    win.getMouse()
    win.close()

#rectangle()

def circle():
    win = GraphWin("Circle", 700, 700)
    center = win.getMouse()
    circumference_click = win.getMouse()
    term1 = (center.getX() - circumference_click.getX()) ** 2
    term2 = (center.getY() - circumference_click.getY()) ** 2
    radius = math.sqrt(term1 + term2)
    circle1 = Circle(center, radius)
    circle1.draw(win)
    message1 = Text(Point(600, 650), "Radius:\n" + str(radius))
    message2 = Text(Point(350, 650), "Click to end the program")

    message1.draw(win)
    message2.draw(win)
    win.getMouse()
    win.close()

#circle()


def pi2():
    sum1 = 0
    first = eval(input("Enter the number of terms to sum"))
    denom = 1
    sign = 1
    for _ in range(first):
        sum1 = sum1 + (4 / denom) * sign
        denom = denom + 2
        sign = sign * -1
    print("pi approximation:", sum1)
    accuracy = math.pi - sum1
    print("accuracy:", abs(accuracy))

#pi2()

if __name__ == '__main__':
    pass