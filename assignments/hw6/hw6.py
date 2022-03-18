"""
Name: <Mena Hakim>
<ProgramName>.py

Problem: <Working with strings
Writing functions that accept arguments and return values.
Modifying an object in a parameter
>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Blake, Sam>
"""
import math


def cash_converter():
    number = eval(input("Enter an integer"))
    print("$" + "{:.2f}".format(number))


def encode():
    message = input("Enter a message ")
    key = eval(input("Enter a key "))
    acc = ""
    for i in message:
        var = ord(i)
        shift = var + key
        switch = chr(shift)
        acc = acc + switch
    print(acc)


def sphere_area(radius):
    formula = 4 * math.pi * (radius ** 2)
    return formula


def sphere_volume(radius):
    formula = (4 / 3) * math.pi * (radius ** 3)
    return formula

def sum_n(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + i
    return acc


def sum_n_cubes(number):
    acc = 0
    for i in range(number + 1):
        acc = acc + (i ** 3)
    return acc


def encode_better():
    message = input("Enter a message: ")
    key = input("Enter a key: ")
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
    print(acc)


if __name__ == '__main__':
    # cash_converter()
    # encode()
    # res = sphere_area(13)
    # print(res)
    # res = sphere_volume(13)
    # print(res)
    # res = sum_n(100)
    # print(res)
    # res = sum_n_cubes(13)
    # print(res)
    encode_better()
    pass
