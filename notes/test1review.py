for i in range(5):
    print (i*i)

for d in [3,1,4,1,5]:
    print (d, end="")

for i in range(4):
    print("Hello", end="!!!")

for i in range(7,3,-1):
    print(i, 2**i)



def horsepower():
    inputhp = eval(input("Enter the number of watts"))
    onehorsepower = 745.7

    convert = inputhp * onehorsepower
    print(convert)