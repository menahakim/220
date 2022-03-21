# for loop is a definite loop / you know when it starts and ends
# indefinite/conditional loops don't necessarily know when they will end
# while loop = while <condition>:
#                    <body>
# as long as condition is still true the loop will continue to run
from graphics import *


# def first_while():
#     for i in range(5):
#         print(i, end=' ')
#     print('\n{0:*<70}'.format(''))
#
#     i = 0
#     while i < 5:
#         print(i, end=' ')
#         i = i + 1
#
#
# def is_equal(p1, p2):  # testing if 2 different points are equal
#     return p1.getX() == p2.getX() and p1.getY() == p2.getY()  # down to 1 line instead of 4 (if)


# MORE BOOL OPERATORS (OR and NOT)

# With the OR bool, if either conditions are true then the statement is true

# With NOT bool, Reverses a statement if P is true then not P is false vice versa

# When there are no parenthesis for order of operations
# You do 1. Not 2. And 3. Or
# functions should be single purpose

# def is_game_over(player_one_points, player_two_points):
#     over_fifteen = player_one_points >= 21 or player_two_points >= 21
#     won_by_two = abs(player_one_points - player_two_points) >= 2
#     skunked = player_one_points >= 7 and player_two_points == 0 or player_two_points >= 7 and player_one_points == 0
#     if over_fifteen and won_by_two or skunked:
#         return True
#     return False
#
#
# def deMorgan_one(a, b):
#     return not(a or b) == (not a and not b)
#
# def deMorgan_test():
#     tests = [[True, True], [True, False], [False, True], [False, False]]
#     for test in tests:
#         a = test[0]
#         b = test[1]
#         result = deMorgan_one(a, b)
#         print('input: {}, output: {}'.format(test, result))


# if __name__ == '__main__':
    # deMorgan_test()
    # player_1 = 0
    # player_2 = 0
    # while not is_game_over(player_1, player_2):
    #     one_points, two_points = eval(input("Enter score for player one and two: "))
    #     player_1 = player_1 + one_points
    #     player_2 = player_2 + two_points
    #     print(player_1, player_2)
    # print("GAME OVER!")


# MORE ABOUT BOOLEANS
# multiplication equates to and
# addition equates to or
# 0 equates to false
# 1 equates to true
# examples (follow algebraic rules)
# a and false == false
# a and true = a
# a or false = a
# double negatives cancel out: not not a == a


# PROPERTIES
# distributive a or (b and c)
# (a or b) and (a or c)


# DeMorgan's Law # distribute not and switch sign
# not(a or b) == not a and not b
# not(a and b) == not a or not b

# truthy/falsy act like booleans but are different data types

def average_sentinel_enter():
    acc = 0
    count = 0
    num = 0
    while num != "":
        acc = acc + eval(num)
        count = count + 1
        num = input("Enter a number (negative to stop)>> ")
    print("average: {}".format(acc / (count - 1)))


def average_file():  # for loop, looping through lines of file
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    for line in file:
        acc = acc + eval(line)
        count = count + 1
    print("average: {}".format(acc / (count - 1)))


def average_file_while():  # while loop version
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != "":
        acc = acc + eval(line)
        count = count + 1
        line = file.readline()
    print("average: {}".format(acc / (count - 1)))


def average_file_nested():  # while loop version
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != "":
        # line = '4,5,6'
        nums_string = line.split(",")  # ['4', '5', '6']
        for num in nums_string:
        acc = acc + eval(num)
        count = count + 1
        line = file.readline()
    print("average: {}".format(acc / (count - 1)))

if __name__ == '__main__':
    average_sentinel_enter()