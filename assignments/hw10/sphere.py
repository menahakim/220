import math


class Sphere:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_surface_area(self):
        return 4 * math.pi * self.radius ** 2

    def get_volume(self):
        return 4 / 3 * (math.pi * self.radius) ** 3

