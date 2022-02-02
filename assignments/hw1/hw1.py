"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""


def calc_rec_area():
    length = eval(input("Enter Length:"))
    width = eval(input("Enter Width:"))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter Length:"))
    width = eval(input("Enter Width:"))
    height = eval(input("Enter Height"))

    total = length * width * height

    print(total)


def shooting_percentage():
    totalshots = eval(input("Enter the Players total shots:"))
    totalmade = eval(input("Enter the total shots the player made:"))

    percentage = totalmade / totalshots * 100
    print(percentage)


def coffee():
    poundamount = eval(input("How many pounds of coffee would you like? "))

    coffeecostperpound = 10.50
    shippingcostperpound = 0.86
    overhead = 1.50

    total = (poundamount * 10.50) + (poundamount *0.86) +1.50
    print(total)



def kilometers_to_miles():
    kilometer = eval(input("How many kilometers did you travel? "))
    convert = 0.621371
    miles = kilometer * convert
    print("Thats", miles, "Miles!")


if __name__ == '__main__':
    pass
