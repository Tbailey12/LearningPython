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

# create the enemy turtle
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('circle')
enemy.penup()
enemy.speed(0)
enemy.setposition(-200, 250)

enemy_speed = 2

# create player bullet
bullet = turtle.Turtle()
bullet.color('yellow')
bullet.shape('triangle')
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bullet_speed = 20

# define bullet state
# ready - ready to fire
# fire - bullet is fired
bullet_state = 'ready'


def move_left():
    """
    move player left
    :return: none
    """
    x = player.xcor()  # gets player xcoord
    x -= player_speed
    if x < -280:  # boundary checking
        x = -280
    player.setx(x)


def move_right():
    """
    move player right
    :return: none
    """
    x = player.xcor()  # gets player xcoord
    x += player_speed
    if x > 280:  # boundary checking
        x = 280
    player.setx(x)


def player_shoot():
    global bullet_state

    if bullet_state == 'ready':
        bullet_state = 'fire'
        # move the bullet to player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x, y)
        bullet.showturtle()


# create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(player_shoot, "space ")

# main game loop
while True:
    # move the enemy
    x = enemy.xcor()
    x += enemy_speed
    enemy.setx(x)

    if enemy.xcor() > 280:
        enemy_speed *= -1  # change direction at boundary
        y = enemy.ycor()
        y -= 40  # drop down a level at boundary
        enemy.sety(y)
    elif enemy.xcor() < -280:
        enemy_speed *= -1
        y = enemy.ycor()
        y -= 40
        enemy.sety(y)

    # move the bullet if it is on the screen
    if bullet_state == 'fire':
        y = bullet.ycor()
        y += bullet_speed
        bullet.sety(y)
        if bullet.ycor() > 280:
            bullet.hideturtle()
            bullet_state = 'ready'

# turtle.done()
# delay = input('Press enter to close')
