class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.birthday = ''
        self.salary = 0

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_birthday(self):
        return self.salary

    def set_birthday(self, birthday):
        self.__parse_birthday(birthday)

    def __parse_birthday(self, birthday):  # double __ means its private no one can access it outside the class


    def get_salary(self):
        return self.salary

    def set_salary(self, salary):
        self.salary = salary


