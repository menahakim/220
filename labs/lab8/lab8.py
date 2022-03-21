from graphics import *
from random import randint
import math
import time


def main():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)

    circle_one = Circle(Point(100, 200), 10)
    circle_one.setFill(get_random_color())
    circle_one.draw(win)
    circle_two = Circle(Point(400, 500), 10)
    circle_two.setFill(get_random_color())
    circle_two.draw(win)
    xvelocity1 = get_random(15)
    xvelocity2 = get_random(15)
    yvelocity1 = get_random(15)
    yvelocity2 = get_random(15)
    while True:
        time.sleep(0.025)
        circle_one.move(xvelocity1, yvelocity1)
        circle_two.move(xvelocity2, yvelocity2)
        if did_collide(circle_one, circle_two):
            xvelocity1 = xvelocity1 * -1
            yvelocity1 = yvelocity1 * -1
            xvelocity2 = xvelocity2 * -1
            yvelocity2 = yvelocity2 * -1
        if hit_vertical(circle_one, win):
            xvelocity1 = xvelocity1 * -1
        if hit_horizontal(circle_one, win):
            yvelocity1 = yvelocity1 * -1
        if hit_vertical(circle_two, win):
            xvelocity2 = xvelocity2 * -1
        if hit_horizontal(circle_two, win):
            yvelocity2 = yvelocity2 * -1


def did_collide(circle_one, circle_two):
    xdistance = (circle_two.getCenter().getX() - circle_one.getCenter().getX())
    ydistance = (circle_two.getCenter().getY() - circle_one.getCenter().getY())
    sum = math.sqrt((xdistance)**2 + (ydistance)**2)
    getradius = circle_one.getRadius() + circle_two.getRadius()
    if getradius >= sum:
        return True
    else:
        return False


def get_random(move_amount):
    return randint(-move_amount, +move_amount)


def hit_vertical(ball, win):
    if ball.getCenter().getX() - ball.getRadius() <= 0:
        return True
    if ball.getCenter().getX() + ball.getRadius() >= win.getWidth():
        return True
    else:
        return False

def hit_horizontal(ball, win):
    if ball.getCenter().getY() - ball.getRadius() <= 0:
        return True
    if ball.getCenter().getY() + ball.getRadius() >= win.getHeight():
        return True
    else:
        return False


def get_random_color():
    red = randint(0, 255)
    green = randint(0,255)
    blue = randint(0,255)
    return color_rgb(red, green, blue)


main()