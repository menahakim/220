grades_tbe = eval(input("How many grades will you enter?"))
sumvariable = 0

def average():
    for i in range(grades_tbe):
        grades = eval(input("Enter Grade"))
        sumvariable = grades + sumvariable
        print(sumvariable)
