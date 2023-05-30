import turtle
import math 
import random 

turtle1 = turtle.Turtle()
turtle1.shape("turtle")
turtle1.color("purple")
turtle1.speed(4)
window = turtle.Screen()
turtle1.home()
dimensions = turtle.screensize()
distance = 10
angle = 90
is_in_screen = True
while is_in_screen:
    coin = random.randrange(0,2)
    if coin: #heads
        turtle1.right (angle)
    else: #tails
        turtle1.left(angle)
    turtle1.forward(distance)

    x = turtle1.xcor()
    y = turtle1.ycor()

    x_range = window.window_width() / 2
    y_range = window.window_height() / 2

    if abs(x) > x_range or abs(y) > y_range:
        is_in_screen = False 

#x = random.randrange (0,400)
#y = random.randrange (0,300)

turtle1.goto(x, y)



window.exitonclick() 
