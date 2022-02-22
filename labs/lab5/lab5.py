from graphics import *
import math


def triangle():
    width = 750
    height = 750
    win = GraphWin("Triangle,", width, height)
    corner1 = win.getMouse()
    corner2 = win.getMouse()
    corner3 = win.getMouse()
    shape = Polygon(corner1, corner2, corner3)
    shape.draw(win)
    distx1 = abs(corner2.getX() - corner1.getX())
    distx2 = abs(corner3.getX() - corner2.getX())
    distx3 = abs(corner1.getX() - corner2.getX())
    disty1 = abs(corner2.getY() - corner1.getY())
    disty2 = abs(corner3.getY() - corner2.getY())
    disty3 = abs(corner1.getY() - corner2.getY())
    length1 = math.sqrt((distx1 ** 2) + (disty1 ** 2))
    length2 = math.sqrt((distx2 ** 2) + (disty2 ** 2))
    length3 = math.sqrt((distx3 ** 2) + (disty3 ** 2))
    perimeter = length1 + length2 + length3
    s = perimeter / 2
    area = math.sqrt(s*(s-length1)*(s-length2)*(s-length3))
    message1 = Text(Point(350, 400), "Perimeter:\n" + str(perimeter))
    message2 = Text(Point(350, 450), "Area:\n" + str(area))
    message3 = Text(Point(350, 500), "Click to end the program")
    message1.draw(win)
    message2.draw(win)
    message3.draw(win)

    win.getMouse()
    win.close()


def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red = Entry(Point(win_width / 2 + 50, red_text_pt), 20)
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green = red.clone()
    green.move(0, 30)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue = red.clone()
    blue.move(0, 60)

    # display rgb text
    red_text.draw(win)
    red.draw(win)
    green_text.draw(win)
    green.draw(win)
    blue_text.draw(win)
    blue.draw(win)
    shape.setFill(color_rgb(red, green, blue))

    # Wait for another click to exit
    win.getMouse()
    win.close()


color_shape()


def process_string():
    sentence = input("Enter a sentence: ")
    print(sentence)
    first = sentence[0]
    print(first)
    last = sentence[-1]
    print(last)
    inclusive = sentence[1:4]
    print(inclusive)
    concat = first + last
    print(concat)
    first3 = sentence[0:2] * 10
    print(first3)
    for i in sentence:
        print(i)
    chars = len(sentence)
    print(chars)


def process_list():
    pt = Point(5, 10)
    values = [5, 'hi', 2.5, 'there', pt, '7.2']

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] * 5
    print(x)
    x = values[2:5]
    print(x)
    x = values[2:4] + [values][0]
    print(x)
    x = values[2] + values[0] + float(values[5])
    print(x)
    x = values[0] + values[2] + float(values[5])
    print(x)
    x = len(values)
    print(x)


def another_series():  # using mod %
    acc = 0
    total = 0
    terms = eval(input("Enter the number of terms: "))
    for i in range(terms):
        acc = acc % 6
        acc += 2
        print(acc, end=" ")
        total = total + acc
    print("\n", "sum = ", total)


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
