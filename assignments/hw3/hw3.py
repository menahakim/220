"""
Name: <your name goes here – first and last>
<ProgramName>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>
"""



def average():
    grades_tbe = eval(input("How many grades will you enter?"))
    sum_num = 0

    for _ in range(grades_tbe):
        grades = eval(input("Enter Grade"))
        sum_num = sum_num + grades
        total = sum_num / grades_tbe

    print(total)



def tip_jar():
    sum_num = 0
    for _ in range(1,6):
        donation = eval(input("How much would you like to donate?"))
        sum_num = sum_num + donation

    print("total tips:", sum_num)



def newton():
    number = eval(input("What number would you like to square root?"))
    approx = eval(input("How many times would you like to improve the approximation"))
    final = number  # This is to for the second run of the for loop

    for i in range(approx):
        final = (final + number/final) / 2
        i -= 1
    print("the square root is approximately:", final)


def sequence():
    terms = eval(input("Enter the amount of terms:"))
    variable = -1
    for i in range(terms):
        variable = ((i + 1) % 2) * 2 + variable
        print(variable, end=" ")


def pi():
    terms = eval(input("Enter the amount of terms:"))
    denom = 1
    numerator = 0
    product = 1
    for i in range(terms):
        denom = (i % 2 * 2) + denom
        numerator = (i + 1) % 2 * 2 + numerator
        product = product * (numerator / denom)

    print(product * 2)


if __name__ == '__main__':
    pass
