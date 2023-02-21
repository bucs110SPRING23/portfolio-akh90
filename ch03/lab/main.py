import turtle #1. import modules
import random

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

screen.fill ("blue")
pygame.display.flip()
pygame.time.wait(1000)

#points = []
#num_sides = 
#side_length =
#xpos = 
#ypos = 

pygame.draw.polygon (screen, "black", [[100,100], [150,300], [100,200]])
pygame.time.wait (1000)
pygame.draw.polygon (screen, "black", [[700,-200], [550,200], [500,100], [750, 300]])
#for _ in range (3):
#    angle = 360/num_sides


pygame.display.flip()
pygame.time.wait (1000)
