import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

    def distance_to(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

if __name__ == "__main__":
    point1 = Point(0, 0)
    point2 = Point(3, 4)
    print(point1)
    print(point2)

    distance = point1.distance_to(point2)
    print(f"Distance between the points: {distance}")
