import random
from turtle import Turtle,Screen
import random


def start_race(turtles):
    is_race_on = True
    winner = ''
    while is_race_on:
        for tim in turtles:
            step = random.randint(0, 10)
            tim.forward(step)
            if tim.xcor() > 230:
                winner = tim.pencolor()
                is_race_on = False

    return winner


def check_bet_won(winner, bet):
    result = ''
    if bet == winner:
        result = f'your bet for {bet} won :) {winner} indeed knock this race'
    else:
        result = f'your bet for {bet} lost :( {winner} has won this race'
    return result


def create_turtles():
    colors = ['red', 'blue', 'green', 'black', 'purple']
    x_axis = -230
    y_axis = [-100, -50, 0, 50, 100]
    turtles = []

    for i, y in enumerate(y_axis):
        tim = Turtle(shape="turtle")
        tim.penup()
        tim.goto(x_axis, y)
        tim.color(colors[i])
        turtles.append(tim)

    return turtles


def main():
    screen = Screen()
    screen.setup(width=500, height=400)
    bet = screen.textinput(title='Make your bet', prompt="Which turtle would win the race")
    turtles = create_turtles()
    winner = start_race(turtles)
    print(check_bet_won(winner, bet))
    screen.exitonclick()


if __name__ == '__main__':
    main()

