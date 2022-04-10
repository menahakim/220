from graphics import *


class Face:
    def __init__(self, window, center, size):
        eye_size = 0.15 * size
        eye_off = size / 3.0
        mouth_size = 0.8 * size
        mouth_off = size / 2.0
        self.window = window
        self.head = Circle(center, size)
        self.head.draw(window)
        self.left_eye = Circle(center, eye_size)
        self.left_eye.move(-eye_off, -eye_off)
        self.right_eye = Circle(center, eye_size)
        self.right_eye.move(eye_off, -eye_off)
        self.left_eye.draw(window)
        self.right_eye.draw(window)
        point_1 = center.clone()
        point_1.move(-mouth_size / 2, mouth_off)
        point_2 = center.clone()
        point_2.move(mouth_size / 2, mouth_off)
        self.mouth = Line(point_1, point_2)
        self.mouth.draw(window)

    def smile(self):
        center_mouth = self.mouth.getCenter()# save the center point from self.mouth
        center_mouth.undraw()#undraw self.mouth
        self.mouth = Polygon(self.mouth.getCenter())#set self.mouth equal to a new triangle with the same center point
        self.mouth.draw()


    def shock(self):
        center_mouth = self.mouth.getCenter()  # save the center point from self.mouth
        center_mouth.undraw()
        self.mouth = Circle(Point(self.mouth.getCenter), 10)
        self.mouth.draw()
        pass

    def wink(self):
        self.left_eye = self.left_eye.getCenter()# save the center point from self.left_eye
        smile = smile(self)  #call smile() to change mouth
        self.left_eye.undraw()  #undraw self.left_eye
        self.left_eye = Line(150, 350) #set self.left_eye equal to a new line with the same center point
        self.left_eye.draw() #draw self.left_eye
        pass


def main():
    win = GraphWin("Face", 500, 500)
    center = (Point(250, 250))
    size = 250

    my_face = Face(win, center, size)
    win.getMouse()


main()

