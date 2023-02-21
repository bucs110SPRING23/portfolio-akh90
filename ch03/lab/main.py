import turtle #1. import modules
import random

x = random.randrange (1,10)
print (x)

#Part A
window = turtle.Screen() # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')
leonardo.speed(1)
michelangelo.speed(1)
michelangelo.up() # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. Your PART A code goes here
turtle.delay (20)
leonardo.forward (100)
michelangelo.forward (50)
turtle.ontimer (20)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for _ in range (3):
    turtle.ontimer (30)
    leonardo.forward (random.randrange(1,10))
    michelangelo.forward (random.randrange(1,10))
    
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

# PART B - complete part B here
import pygame
import math

pygame.init()
screen = pygame.display.set_mode()

screen.fill ("cornflowerblue")
pygame.display.flip()
pygame.time.wait(200)

shap_sides = [3, 4, 6, 20, 100, 360]
for x in shap_sides:
    points = []
    num_sides = x
    side_length = 200
    xpos = 500
    ypos = 300

    for _ in range (num_sides):
        angle = 360/num_sides
        radians = math.radians(angle * _)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])

      
    pygame.draw.polygon (screen, "darkviolet", points)
    pygame.time.wait (1000)
    pygame.display.flip()
    screen.fill ("cornflowerblue")
   
