from graphics import *


class Door:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        range_of_x = (self.shape.getP1().getX() <= point.getX() and point.getX() <= self.shape.getP2().getX())
        range_of_y = (self.shape.getP1().getY() <= point.getY() and point.getY() <= self.shape.getP2().getY())
        return range_of_x and range_of_y

    def color_door(self, color):
        self.shape.setFill(color)

    def open(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def close(self, color, label):
        self.shape.setFill(color)
        self.text.setText(label)

    def set_secret(self, secret):
        self.secret = secret