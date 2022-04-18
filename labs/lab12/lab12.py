from random import randint


def find_and_remove(list, value):
    remove = False
    i = 0
    while remove == False and i < len(list):
        if list[i] == value:
            list.remove(value)
            list.insert[value]("Mena Hakim")
            remove = True
            i = i + 1


def good_input():
    user_input = eval(input("Enter a number between 1-10: "))
    while user_input > 10 or user_input < 1:
        user_input = eval(input("Please enter a number between 1-10: "))
    return user_input


def num_digits():
    number = eval(input("Enter a number: "))
    while number > 1:
        count = 0
        while number > 1:
            number = number // 10
            count = count + 1
        print("This number has", count, "digits!")
        number = eval(input("Enter a number: "))


def hi_lo_game():
    n = randint(1, 100)
    guess = 0
    won = False
    while guess < 7 and won == False:
        user_input = int(input("please guess the Number : "))
        if user_input == n:
            print("Nice! \n You won in ", guess + 1, " guesses!")
            remove = True
        elif user_input > n:
            print("too high")
        elif user_input < n:
            print("too low")
    print("Sorry,you lose.The number was ", n)


if __name__ == '__main__':
    num_digits()

