from graphics import *
from button import Button
from door import Door


def main():
    width = 500
    height = 500
    win = GraphWin("Test", width, height)
    win.setBackground('white')

    button_shape = Rectangle(Point(130, 50), Point(375, 100))
    button_label = 'Exit'
    button = Button(button_shape, button_label)
    button.color_button('red')
    button.draw(win)

    door_shape = Rectangle(Point(190, 105), Point(310, 400))
    door_label = 'Closed'
    door = Door(door_shape, door_label)
    door.color_door('blue')
    door.draw(win)

    while button.is_clicked(win.getMouse()) is False:
        mouse_click = win.getMouse()
        if door.is_clicked(mouse_click) is True and door.get_label() == 'Closed':
            door.open('yellow', 'Open')
        elif door.is_clicked(mouse_click) is True and door.get_label() == 'Open':
            door.close('green', 'Closed')
        elif button.is_clicked(mouse_click) is True:
            win.close()

main()