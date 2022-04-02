# student has name, hours, quality_points which are instance variables
# our method is get_gpa()
# class to calculate gpa
class Student:
    def __init__(self, name, hours, quality_points):
        self.name = name
        self.hours = float(hours)
        self.quality_points = float(quality_points) # use float so we are not dealing with strings

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_gpa(self):
        return self.quality_points / self.hours
