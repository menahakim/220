from graphics import *


def get_nums():
    nums = []
    user_input = input("Enter a number(enter to quit): ")
    while user_input != "":
        nums.append(eval(user_input))
        user_input = input("Enter a number (enter to quit): ")
    return nums


def mean(nums):
    acc = 0
    for number in nums:
        acc += number
    return acc / len(nums)


def std_dev(nums, avg):  # standard deviation
    acc = 0
    for num in nums:
        acc += (avg - num) ** 2
    return (acc / (len(nums) - 1)) ** 0.5


def median(nums):
    nums.sort()
    middle_index = len(nums) // 2
    if len(nums) % 2 == 0:
        right_middle = nums[middle_index]
        left_middle = nums[middle_index -1]
        return (right_middle + left_middle / 2)
    else:
        return nums[middle_index]


def x_sort(circle):
    return circle.getCenter().getX()


def print_c(circles):
    for circle in circles:
        print('({}, {})'.format(circle.getCenter().getX(),
                                circle.getCenter().getY(),
                                circle.getRadius()), end=" | ")


def main():
    c1 = Circle(Point(20, 30), 90)
    c2 = Circle(Point(2, 3), 909)
    c3 = Circle(Point(25, 39), 9)
    c4 = Circle(Point(208, 3), 990)
    circles = [c1, c2, c3, c4]
    print_c(circles)
    circles.sort(key=x_sort)  # we are just passing x_sort in not running it does not need parenthesis
    print_c(circles)
    numbers = get_nums()
    # mean
    avg = mean(numbers)
    # std_dev
    s = std_dev(numbers, avg)
    print(numbers, avg)


if __name__ == '__main__':
    main()


# lists and tuples can use the same operations
# the difference is tuples can not be edited if you want to make a change you have to make a new tuple
# tuples can not use mutable operations
# you can use .count and .index methods