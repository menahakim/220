from graphics import *


def vigenere():
    width = 500
    length = 500
    win = GraphWin("Vigenere", width, length)
    messagetext = Text(Point(50, 100), "Message to code: ")
    keyword = Text(Point(75, 150), "Enter Keyword")
    close = Text(Point(250, 450), "Click Anywhere to Close Window")
    messagetext.draw(win)
    keyword.draw(win)
    messagebox = Entry(Point(50, 130), 10)
    keywordbox = Entry(Point(75, 180), 10)
    button = Rectangle(Point(200, 250), Point(300, 300))
    buttontext = Text(Point(250, 270), "Encode")
    button.draw(win)
    buttontext.draw(win)
    messagebox.draw(win)
    keywordbox.draw(win)
    win.getMouse()
    button.undraw()
    buttontext.undraw()
    message = messagebox.getText()
    key = keywordbox.getText()
    message = message.upper()
    key = key.upper()
    keyindex = 0
    acc = ""
    for i in range(len(message)):
        messageval = ord(message[i]) - ord("A")
        keyval = ord(key[keyindex]) - ord("A")
        subtotal = messageval + keyval
        total = subtotal % 26  # modding by 26 so it looks back to A after Z
        total = total + ord("A")  # restoring ascii values that were subtracted line 65-66
        total = chr(total)  # converting ascii values back to characters
        acc = acc + total  # adding total to accumulator
        keyindex = keyindex + 1
        keyindex = keyindex % len(key)
    decodedmessage = Text(Point(250, 400), acc)
    decodedmessage.draw(win)

    close.draw(win)
    win.getMouse()
    win.close()


vigenere()