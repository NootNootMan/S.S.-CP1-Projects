import random
import turtle as t


player = t.Turtle()
player.color('blue')
player.shape('turtle')

wall = t.Turtle()
wall.color('black')
wall.hideturtle()
wall.speed(0)
wall.pensize(2)
wall.penup()
wall.setpos(-200, -200)
wall.pendown()
wall.setheading(0)
wall.forward(600)
wall.setheading(90)
wall.forward(600)
wall.setheading(360)
wall.forward(-600)
wall.setheading(270)
wall.forward(600)



while True:

    move = input("Wasd to move!")
    if move == 'd':
        player.setheading(0)
        player.forward(50)
    if move == 'a':
        player.setheading(360)
        player.forward(-50)
    if move == 'w':
        player.setheading(90)  
        player.forward(50)    
    if move == 's':
        player.setheading(270)
        player.forward(50)


t.done()

