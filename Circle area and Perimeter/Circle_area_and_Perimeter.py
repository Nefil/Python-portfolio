
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area_of_circle(self):
        return 3.14 * self.radius ** 2

    def perimeter_of_circle(self):
        return 2 * 3.14 * self.radius

circle = Circle(4)
area = circle.area_of_circle()
perimeter = circle.perimeter_of_circle()

print("Area of circle is:", area)
print("Perimeter of circle is:", perimeter)