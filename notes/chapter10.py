# CLASSES / OBJECTS
#         INSTANCE of class

# a class is a structure that helps us organize our data
# classes will contain data and functionality that you can do with that data
# for example the data a circle contains are the center and radius
# move(), getCenter(), getRadius()
# what is it, what does it have, what does it do
# c = Circle(Point(3, 4), 10)
# object   Constructor
# d = Circle(Point(9, 5), 15)
# c and d are different INSTANCES same class/data type

# creating a CAR class
# What a car has - number of seats, color, engine, mileage, location - INSTANCE VARIABLES
# What a car does - turn(), drive(), roll_windows(), beep() - METHODS
# INSTANCE variables are accessed or changed by the methods
# bmw = Car(4, "red", 3, 3, 300)
# bmw.drive(30)
from die import Die
from studentgpa import Student
from Employee import Employee


def print_employee(employee):
    print('{}. {} - {} - {}'.format(employee.get_id(), employee.get_name(), employee.get_birthday(), employee.get_salary))


def main():
    e = Employee("John", 1)
    e.set_salary(100000)
    print_employee(e)
    f = Employee("Alice", 7)
    # student_file = open('student.txt', 'r')
    # student_file.readline()
    # students = []
    # for line in student_file.readlines():
    #     split_student = line.split(',')
    #     name = split_student[0]
    #     hours = split_student[1]
    #     points = split_student[2]
    #     student = Student(name, hours, points)
    #     students.append(student)
    #     print(student.get_gpa())
    # for student in students:
    #     print(student.get_name())
    # number_of_sides = eval(input("How many sides?"))
    # d = Die(number_of_sides)
    # playing = True
    # while playing:
    #     d.roll()
    #     print(d.get_value())
    #     stopping = input('hit enter to roll')
    #     playing = not stopping


if __name__ == '__main__':
    main()
