from graphics import Point, GraphWin, Polygon, Text
import time

def valentine ():
    width = 700
    height = 700
    win = GraphWin("Valentine", width, height)

    words1 = Point(width / 2, height -30)
    words2 = Text(words1, "Happy Valentine's Day!")

    heart = Polygon(Point(350, 500), Point(200, 250), Point(220, 220), Point(260, 200), Point(350, 300),
                    Point(440, 200), Point(480, 220), Point(500, 250))
    heart.setFill("Red")

    arrow_x = 100
    arrow_y = 100
    arrow1 = Polygon(Point(arrow_x, (arrow_y + 450)), Point((arrow_x - 10), (arrow_y + 440)),
                     Point((arrow_x + 450), arrow_y), Point((arrow_x + 440), (arrow_y - 10)))
    arrow2 = Polygon(Point((arrow_x + 460), (arrow_y + 10)), Point((arrow_x + 430), (arrow_y - 10)),
                     Point((arrow_x + 450), (arrow_y - 30)))
    arrow1.setFill("Yellow")
    arrow2.setFill("Yellow")
    win.setBackground("Beige")

    arrow1.draw(win)
    arrow2.draw(win)
    words2.draw(win)
    heart.draw(win)
    for _ in range(40):
        arrow1.move(5, -5)
        arrow2.move(5, -5)
        time.sleep(.6)

    instruction_point = Point(width / 2, height - 10)
    instruction = Text(instruction_point, "Click again to close")
    instruction.draw(win)

    win.getMouse()
    win.close()

valentine()