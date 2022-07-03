class Circle:
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter

    def calculate_circumference(self):
        circumference = Circle.__pi * self.diameter
        return circumference

    def calculate_area(self):
        radius = self.diameter / 2
        area = Circle.__pi * radius ** 2
        return area

    def calculate_area_of_sector(self, angle):
        radius = self.diameter / 2
        area_sector = (angle / 360) * Circle.__pi * radius ** 2
        return area_sector

# circle = Circle(10)
# angle = 5
# print(f"{circle.calculate_circumference():.2f}")
# print(f"{circle.calculate_area():.2f}")
# print(f"{circle.calculate_area_of_sector(angle):.2f}")

