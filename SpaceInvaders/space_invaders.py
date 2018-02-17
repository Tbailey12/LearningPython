"""
    File name:          space_invaders.py
    Version:            0.0
    Author:             Tom Bailey
    Date created:       2018-02-17
    Date last modified: 2018-02-17
    Python Version:     3.6

    Description:
    basic space invaders game to practice rendering
"""

import turtle
import os

# screen setup
win = turtle.Screen()
win.bgcolor('black')
win.title('Space Invaders')

# draw game border
border_pen = turtle.Turtle()
border_pen.speed(0)  # 0 is fastest speed
border_pen.pensize(3)
border_pen.color('white')
border_pen.penup()  # pen is not touching canvas
border_pen.setposition(-300, -300)
border_pen.pendown()
for side in range(4):
    border_pen.fd(600)
    border_pen.left(90)
border_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('triangle')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15  # controls the movement speed of the player


# move the player left and right
def move_left():
    x = player.xcor()  # gets player xcoord
    x -= player_speed
    player.setx(x)


def move_right():
    x = player.xcor()  # gets player xcoord
    x += player_speed
    player.setx(x)


# create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

turtle.done()

delay = input('Press enter to close')
