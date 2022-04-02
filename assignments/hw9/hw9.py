import random
from graphics import *


def get_words(file_name):
    word_file = open(file_name, 'r')
    input_file = word_file.read()
    input_list = input_file.split("\n")
    file_list = []
    for line in input_list:
        file_list.append(line)
    return file_list


def get_random_word(words):
    word_index = random.randint(0, len(words) - 1)
    return words[word_index]


def letter_in_secret_word(letter, secret_word):
    for character in secret_word:
        if character == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for character in guesses:
        if character == letter:
            return True
    return False


def make_hidden_secret(secret_word, guesses):
    letter_string = ""
    for character in secret_word:
        if letter_in_secret_word(character, guesses):
            letter_string = letter_string + character
        else:
            letter_string = letter_string + "_"
    return letter_string


def won(guessed):
    for character in guessed:
        if character == "_":
            return False
    return True


def play_graphics(secret_word):
    guesses = []
    guesses_remaining = 6
    window = GraphWin("Hangman", 500, 500)
    hidden_word = Text(Point(400, 400), "******")
    letters_guessed = Text(Point(250, 50), guesses_remaining)
    take_a_guess = Entry(Point(250, 450), 20)
    while True:
        window.redraw()
        hidden_word.draw(GraphWin)
        letters_guessed.draw(GraphWin)
        take_a_guess.draw(GraphWin)
        print('Already guessed: ', guesses)
        print("You have", guesses_remaining, "guesses remaining.")
        print(make_hidden_secret(secret_word, guesses))
        guess = input('Guess a letter')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif already_guessed(guess, guesses):
            print("You have already guessed this letter")
        elif letter_in_secret_word(guess, secret_word):
            guesses.append(guess)
            if won(make_hidden_secret(secret_word, guesses)):
                print("You won!", "The word was", secret_word)
                exit()
        else:
            guesses_remaining = guesses_remaining - 1
            print("This letter is not in the word")
            incorrect = Circle(Point(250, 100), 5)
            incorrect.draw(GraphWin)
            guesses.append(guess)
            if guesses_remaining == 0:
                print("You lost!", "The word was", secret_word)
                exit()


def play_command_line(secret_word):
    guesses = []
    guesses_remaining = 6
    while True:
        print('Already guessed: ', guesses)
        print("You have", guesses_remaining, "guesses remaining.")
        print(make_hidden_secret(secret_word, guesses))
        guess = input('Guess a letter')
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif already_guessed(guess, guesses):
            print("You have already guessed this letter")
        elif letter_in_secret_word(guess, secret_word):
            guesses.append(guess)
            if won(make_hidden_secret(secret_word, guesses)):
                print("You won!", "The word was", secret_word)
                exit()
        else:
            guesses_remaining = guesses_remaining - 1
            print("This letter is not in the word")
            guesses.append(guess)
            if guesses_remaining == 0:
                print("You lost!", "The word was", secret_word)
                exit()


if __name__ == '__main__':
    words = get_words("words.txt")
    get_random = get_random_word(words)
    # play_command_line(get_random)
    # play_graphics(get_random)
