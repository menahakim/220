from lab10.door import Door
from lab10.button import Button
from graphics import *
import random


def main():
    width = 500
    height = 500
    win = GraphWin("Test", width, height)
    win.setBackground('white')

    button_shape = Rectangle(Point(190, 50), Point(310, 100))
    button_label = 'Exit'
    button = Button(button_shape, button_label)
    button.color_button('red')
    button.draw(win)

    door_shape = Rectangle(Point(190, 105), Point(310, 400))
    door_label = 'Door1'
    door = Door(door_shape, door_label)
    door.color_door('grey')
    door.draw(win)

    door2_shape = Rectangle(Point(30, 105), Point(150, 400))
    door2_label = 'Door2'
    door2 = Door(door2_shape, door2_label)
    door2.color_door('grey')
    door2.draw(win)

    door3_shape = Rectangle(Point(360, 105), Point(460, 400))
    door3_label = 'Door3'
    door3 = Door(door3_shape, door3_label)
    door3.color_door('grey')
    door3.draw(win)

    Text(Point(250, 470), "Click to guess which is the secret door")

win = 0
lose = 0
while True:
    door = [1, 2, 3]
    x = 0


    def correct_answer():
        answer = random.choice(door)
        return answer
    a = correct_answer()

    def pick_guess():
        guess = int(input("Please choose a door (1-3): ").strip())
        return guess

    b = pick_guess()

    if a == b:
        door.color_door('green', 'you got it!')



main()