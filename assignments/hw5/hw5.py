"""
Name: <Mena Hakim>
<ProgramName>.py

Problem: <Use Python strings, lists, indexing, and slicing .>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Blake Easley>
"""


def name_reverse():
    name = input("Enter a name (first last): ")
    name = name.split(" ")
    first = name[0]
    last = name[1]
    print(last + ", " + first)


def company_name():
    domain = input("Enter a domain:")
    domain = domain.split(".")
    print(domain[1])


def initials():
    amount = eval(input("How many students are in the class?"))

    for i in range(amount):
        name = input("What is the name of student " + str(i+1) + ": ")
        name = name.split(" ")
        first = name[0]
        last = name[1]
        print(first[0] + last[0])


def names():
    names1 = input("Enter a list of names seperated by commas ")
    names1 = names1.split(", ")

    for i in names1:
        names2 = i.split(" ")
        print(names2[0][0] + names2[1][0], end=" ")


def thirds():
    amount = eval(input("Enter the number of sentences: "))
    acc = ""

    for i in range(amount):
        sentence = input("Enter sentence " + str(i + 1) + ": ")
        acc = acc + sentence[0::3]
    print(acc)


def word_average():
    sentence = input("Enter a sentence: ")
    words = sentence.split(" ")
    acc = 0
    for i in words:
        acc = acc + len(i)
    print(acc/len(words))


def pig_latin():
    sentence = input("Enter a sentence to convert to pig latin: ")
    sentence = sentence.lower()
    words = sentence.split(" ")
    acc = ""
    for i in words:
        piglatin = i[1:] + i[0] + "ay"  # 1: means the second value AND everything after it
        acc = acc + piglatin + " "
    acc = acc.rstrip()
    print(acc)


if __name__ == '__main__':
    name_reverse()
    company_name()
    initials()
    names()
    thirds()
    word_average()
    pig_latin()









