
# STRINGS are a sequence of characters / use ' ' or " "

# LISTS are sequences of objects (any data type) [ ] what goes inside square brackets are elements

# list example b = [ "paul", "george", "john", "jim" ]  list of strings b would be type 'list'

# mix example [ 3, "Monday", 4, "Tuesday" ] in python you can use these not in java

# len() is how many elements are in a list

# + = CONCATENATION

# for strings "hello" + "world"
# result = "helloworld"

# can not concatenate two different data types

# REPETITION "hi" * 2 = "hihi"

# b * 2 [p, g, j, j, p, g, j, j]

a = "hello world!"
for l in a:
    print(l)
b = [ "paul", "george", "john", "jim" ]
# index 0        1        2       3
for name in b:
    print(name)

# INDEXING position of first element is always 0 position of last element is len(b) - 1
# c = a[7]
# print(c) would be W and is a string

# a group of characters in a string is called a substring a group of elements in a list is a sublist

# access them using SLICING

# <str>[<int>:<int>:<int>]
  #     start  stop  step
# c = a[1:8:2]
# print(c)
# to reverse using splicing [::-1]

# when you slice a list you get a list data type
# b[1:2] is not equal to b[1]

# def get_month()
#   input = eval(input("Enter month"))
#   months = ["January", "February", "March"...]
#   month = month[input -1]
#   print("that's", month)

# days = ["Monday", "Tuesday"]
# days.append("Wednesday") preferred method for adding one thing
# OR days = days + ["Wednesday"] can not add list and string so must put brackets preferred for adding multiple things

# empty lists can be useful for adding user input to the list
# EXAMPLE
# numbers [ ]
# for i in range(10)
#   number=eval(input("Enter a number"))
#   number.append(number)

# a = "hello, world!"
# b = a.upper()
# print(b)
# .upper makes everything uppercase . lower makes everything lowercase
# .count('l') takes a string returns an integer with how many times a parameter appears in an object
# .find marks index value and returns it

# .replace: replaces the string value
# numbers = [1,2,3,4]
# ' 'join(numbers)

# a.center
# a.ljust(10)
# a.rjust(10)

# a.lstrip
# a.rstrip
# a.strip

# c = b.split() can take no parameter or string parameter
# at all spaces it creates a new element in a list

# Encoding
# How do we convert "H" to 1's and 0's
# Unicode standard encoding method
# stores letters to different number values
# ASCII is also another standard encoding method
# A ----> 65  B ----> 66 C ----> 67 etc...
# Decoding going back to original value
# ord() - ordinal string as parameter returns an integer
# ord("A") returns 65
# chr() - character
# chr(97) takes an integer as parameter returns a string

def encode():
    word = input("Enter a word:")
    output = "" # OR
    for letter in word:
        print(ord(letter), end=" ")
        output.append(str(ord(letter))) # 3rd solution
        output = output + str(ord(letter)) + " " # OR HAVE TO CONVERT ORD TO STRING HAVE TO MATCH DATA TYPES
    print(output.rstrip()) # Solution for taking out last space OR
    print(output[:-1]) # another solution for taking out last space
    print(" ").join(output))

encode()

def decode():
    numbers = input("Enter unicode string:")
    num_list = numbers.split()
    output = ""
    for num in num_list:
        output = output + chr(eval(num))
    print(output)



