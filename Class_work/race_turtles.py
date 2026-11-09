#Surabya Satyal Race Turtle Period-1

import turtle as t
import random

green_turtle = t.Turtle()
green_turtle.color('green')
green_turtle.shape('turtle')
green_turtle.penup()
green_turtle.forward(-300)

red_turtle = t.Turtle()
red_turtle.color('red')
red_turtle.shape('turtle')
red_turtle.penup()
red_turtle.goto(0,250)
red_turtle.forward(-300)

blue_turtle = t.Turtle()
blue_turtle.color('blue')
blue_turtle.shape('turtle')
blue_turtle.penup()
blue_turtle.goto(0,-250)
blue_turtle.forward(-300)

green_speed = random.randint(1,5)
green_turtle.speed = green_speed
red_speed = random.randint(1,5)
red_turtle.speed = red_speed
blue_speed = random.randint(1,5)
blue_turtle.speed = blue_speed

green_turtle.pendown()
green_turtle.forward(750)

red_turtle.pendown()
red_turtle.forward(750)

blue_turtle.pendown()
blue_turtle.forward(750)

t.done()


