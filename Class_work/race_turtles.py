#Surabya Satyal Race Turtle Period-1

import turtle as t
import random

#Finish line
finish_line = t.Turtle()
finish_line.hideturtle()
finish_line.speed(0)
finish_line.penup()
finish_line.goto(500,-600)
finish_line.pendown()
finish_line.goto(500, 600)


green_turtle = t.Turtle()
green_turtle.color('green')
green_turtle.shape('turtle')
green_turtle.penup()
green_turtle.forward(-300)

purple_turtle = t.Turtle()
purple_turtle.color('purple')
purple_turtle.shape('turtle')
purple_turtle.penup()
purple_turtle.goto(0,-500)
purple_turtle.forward(-300)


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

orange_turtle = t.Turtle()
orange_turtle.color('orange')
orange_turtle.shape('turtle')
orange_turtle.penup()
orange_turtle.goto(0,500)
orange_turtle.forward(-300)

green_speed = random.randint(1,5)
green_turtle.speed = green_speed
red_speed = random.randint(1,5)
red_turtle.speed = red_speed
blue_speed = random.randint(1,5)
blue_turtle.speed = blue_speed
orange_speed = random.randint(1,5)
orange_turtle.speed = orange_speed
purple_speed = random.randint(1,5)
purple_turtle.speed = purple_speed

green_turtle.pendown()
red_turtle.pendown()
blue_turtle.pendown()
orange_turtle.pendown()
purple_turtle.pendown()


while True: #The Steps system
    blue_turtle.forward(blue_speed)
    red_turtle.forward(red_speed)
    green_turtle.forward(green_speed)
    orange_turtle.forward(orange_speed)
    purple_turtle.forward(purple_speed)

#Checks who won
    if green_turtle.xcor() >= 500:
        print("Green wins")
        break
    elif red_turtle.xcor() >= 500:
        print("Red wins")
        break
    elif blue_turtle.xcor() >= 500:
        print("Blue wins")
        break
    elif orange_turtle.xcor() >= 500:
        print("Orange wins")
        break
    elif purple_turtle.xcor() >= 500:
        print("Purple wins")
        break
    

t.done()


