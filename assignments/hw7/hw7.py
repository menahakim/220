"""
Name: <Mena Hakim>
<ProgramName>.py

Problem: <Writing functions. Reading and writing text files>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: <Blake>
"""
import encryption


def number_words(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    acc = 1
    for i in infile:
        newline = i.split()  # splitting lines
        for j in newline:  # each individual word
            print((str(acc) + " " + j + "\n"), file=outfile)
            acc += 1


def hourly_wages(in_file_name, out_file_name):
    infile = open(in_file_name, "r")
    outfile = open(out_file_name, "w")
    for i in infile:
        newline = i.split()  # splitting into individual strings
        newline[2] = str(float(newline[2]) + 1.65)  # adding bonus to second index
        print((" ".join(newline)), file=outfile)  # writing it to outfile and going to newline



def calc_check_sum(isbn):
    acc = 0
    convert = str(isbn) # converting isbn to string
    for i in range(len(convert)):  # range is length of isbn
        number = int(convert[i]) * (10 - i)  # converting isbn back to integer to perform math
        acc = acc + number
    return acc % 11


def send_message(file_name, friend_name):
    infile = open(file_name, "r")
    outfile = open(friend_name, "w")
    for i in infile:
        print((i + "\n"), file=outfile)  # writing to outfile


def send_safe_message(file_name, friend_name, key):
    infile = open(file_name, "r")
    outfile = open(friend_name, "w")
    for i in infile:
        newline = encryption.encode(i, key)
        print((newline + "\n"), file=outfile)


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    infile = open(file_name, "r")
    padfile = open(pad_file_name, "r")
    outfile = open(friend_name, "w")
    key = padfile.read()
    for i in infile:
        newline = encryption.encode_better(i, key)
        print((newline + "\n"), file=outfile)


if __name__ == '__main__':
    pass