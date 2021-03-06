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
import math
import random

# screen setup
win = turtle.Screen()
win.bgcolor('black')
win.title('Space Invaders')
win.bgpic('bg.gif')

# register the shapes
win.register_shape('invader.gif')
win.register_shape('player.gif')

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

# scoring
score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color('white')
score_pen.penup()
score_pen.setposition(-290, 275)
scorestring = 'Score: %s' % score
score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
score_pen.hideturtle()

# create the player turtle
player = turtle.Turtle()
player.color('blue')
player.shape('player.gif')
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

player_speed = 15  # controls the movement speed of the player

# choose a number of enemies
number_of_enemies = 5
enemies = list()

# add enemies to list
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

# create the enemy turtle
for enemy in enemies:
    # enemy = turtle.Turtle()
    enemy.color('red')
    enemy.shape('invader.gif')
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x, y)

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


collision_distance = 15


def is_collision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < collision_distance:
        return True
    else:
        return False


# create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(player_shoot, "space ")

# main game loop
while True:
    for enemy in enemies:
        # move the enemy
        x = enemy.xcor()
        x += enemy_speed
        enemy.setx(x)

        # move the enemies down at the boundary
        if enemy.xcor() > 280:
            enemy_speed *= -1  # change direction at boundary
            for enemy_inner in enemies:
                y = enemy_inner.ycor()
                y -= 40
                enemy_inner.sety(y)
        elif enemy.xcor() < -280:
            enemy_speed *= -1
            for enemy_inner in enemies:
                y = enemy_inner.ycor()
                y -= 40
                enemy_inner.sety(y)

        if is_collision(bullet, enemy):
            # reset the bullet
            bullet.hideturtle()
            bullet_state = 'ready'
            bullet.setposition(0, -400)
            # reset the enemy
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            enemy.setposition(x, y)
            score += 10
            scorestring = 'Score: %s' % score
            score_pen.clear()
            score_pen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
            enemy_speed = score/10

        if is_collision(enemy, player):
            player.hideturtle()
            enemy.hideturtle()
            print('Game Over')
            break

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
