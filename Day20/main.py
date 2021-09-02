from turtle import Screen
import time
from Snake import Snake
from Food import Food
from ScoreBoard import ScoreBoard


def set_screen():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    return screen


def set_movements(screen, snake):
    screen.listen()
    screen.onkey(snake.up, 'Up')
    screen.onkey(snake.down, 'Down')
    screen.onkey(snake.left, 'Left')
    screen.onkey(snake.right, 'Right')


def start_game(snake, screen, food, scoreboard):
    is_game_on = True

    while is_game_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        #Detect food collison
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        #Detect collison with wall
        if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
            is_game_on = False
            scoreboard.game_over()

        #Detect collison with tail
        for part in snake.parts[1:]:
            if snake.head.distance(part) < 10:
                is_game_on = False
                scoreboard.game_over()

    return 1


def main():
    screen = set_screen()
    snake = Snake()
    food = Food()
    scoreboard = ScoreBoard()
    set_movements(screen, snake)
    screen.tracer(0)
    start_game(snake, screen, food, scoreboard)
    screen.exitonclick()


if __name__ == '__main__':
    main()
