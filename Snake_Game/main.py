import time
from turtle import Screen, Turtle


from food import Food
from scoreboard import Scoreboard
from snake import Snake

# Inicjalizacja ekranu
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")  # Tło czarne
screen.title("Snake")
screen.tracer(0)

snake = Snake()  # Inicjalizacja węża
food = Food()
score = Scoreboard() # Inicjalizacja tablicy wyników


screen.listen()
screen.onkey(snake.up, "Up")  # Ruch w górę
screen.onkey(snake.down, "Down")  # Ruch w dół
screen.onkey(snake.left, "Left")  # Ruch w lewo
screen.onkey(snake.right, "Right")  # Ruch w prawo

game_is_on = True
ignore_collision = True
collision_ignore_counter = 5  # Liczba iteracji, przez które ignorujemy kolizję

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Sprawdzenie kolizji z jedzeniem
    if snake.turtles[0].distance(food) < 15:
        snake.eat()
        food.refresh()
        score.increase_score()

    # Sprawdzenie kolizji ze ścianami
    if snake.turtles[0].xcor() > 290 or snake.turtles[0].xcor() < -290 or snake.turtles[0].ycor() > 290 or snake.turtles[0].ycor() < -290:
        score.end_game()
        game_is_on = False

    # Sprawdzenie kolizji z samym sobą
    if not ignore_collision:  # Kolizja sprawdzana tylko po zakończeniu fazy ignorowania
        for segment in snake.turtles[1:]:
            if snake.turtles[0].distance(segment) < 10:
                score.end_game()
                game_is_on = False
    else:
        collision_ignore_counter -= 1
        if collision_ignore_counter <= 0:
            ignore_collision = False

screen.exitonclick()