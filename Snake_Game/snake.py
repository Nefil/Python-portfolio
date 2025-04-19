from turtle import Turtle
move_distance = 20  # Odległość, o którą wąż się porusza
x_position = [-20, 0, 20] # Pozycje startowe segmentów węża

class Snake():
    def __init__(self):
        self.turtles = []  # Lista przechowująca segmenty węża
        self.create_snake()

    def create_snake(self):
        for square in range(3):
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x_position[square], 0)
            self.turtles.append(new_turtle)

    def move(self):
        for turtle in range(len(self.turtles) -1, 0, -1):
            new_x = self.turtles[turtle -1].xcor()
            new_y = self.turtles[turtle -1].ycor()
            self.turtles[turtle].goto(new_x, new_y)
        self.turtles[0].forward(move_distance)  # Przesunięcie głowy węża

    def up(self):
        if self.turtles[0].heading() != 270:
            self.turtles[0].setheading(90)

    def down(self):
        if self.turtles[0].heading() != 90:
            self.turtles[0].setheading(270)

    def left(self):
        if self.turtles[0].heading() != 0:
            self.turtles[0].setheading(180)

    def right(self):
        if self.turtles[0].heading() != 180:
            self.turtles[0].setheading(0)

    def eat(self):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(1000, 1000)
        self.turtles[-1].position()  # Ustawienie pozycji nowego segmentu
        self.turtles.append(new_turtle)  # Dodanie segmentu do węża


