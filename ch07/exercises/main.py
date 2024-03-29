
#managing complexity - advanced programming just manages complexity
# -Unix ~10,000 lines of code (SLOC- source lines of code)
# -Chrome ~10,000,000 SLOC
# -OS (windows, ect) ~100,000,000 SLOC

#complex Objects
# -primitives: int, str, float, lists, dict, tuple
# -turtle: x (int), y, heading, color(color), pensize(int), shape(str)
# -myturtle: { x:0, y:0, heading:0, color: (0,0,0), pensize: 1, shape: "turtle"} (dont want to have to do this, tedious)

#bundle data and functions together
# -state: the current values of the data in the object
# -behavior: the functions that operate on the data in the object

# Point (plots points on screen as you tap)
# -object should do one thing
# state: x,y,color
#behavior: change_color, move
"""
#classes == Type
import turtle

t = turtle.Turtle
print (type(t)) #complex
print (type(1)) #primitive


# classes are blueprints for objects
# -functions are stored algorithms 
# -think of a class as a stored data type
# -classes are not executable
# -dont put executable code in global scope, definitions are fine

# Point class
# -instance: an object created from a specifc class
#    t = turtle.Turtle() -> t is an instance of Turtle
# -instance variable: an internal variable that is part of an instance
#    t.x, t.pos -> x and pos are instance variables
# -interfaceL the functions and variables of an object
#    t.forward() -> forward() is a part of the interface of turtle

# Point -make it a class ourselves
### point.py
#def make_point(x,y):
class Point:
    #user types (classes) are always capital
    #usually, classes go in their own file
    #1 class per file
    #dunder = double underscore on both sides of the name
    #adding self.var ties the scope of the variable to the object scope


    def __init__(self):     #self is the instance being created 
        self.x = 0 #dot operator accesses instance variables of an object 
        self.y = 0
        self.color = ""
"""

###main.py
import point
import turtle
import random 
import pygame

pygame.init()
display = pygame.display.set_mode()
""""
points = []
for p in range (10):
    x = random.randint (0,250)
    y = random.randint(0,250)
    p = point.Point(x,y)
    p.random_color()
    points.append(p)

#p1 = point.LED(x=100, y=100)


pygame.draw.circle(display, p.color, (p.rect.x, p.rect.y), p.radius)

while True:

    pygame.display.flip()
"""


def mainloop(display):
    points = []
    #mainloop
    while True:
        #eventloop, goes through for the number of points 
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False
                for i,p in enumerate(points):
                    if p.rect.collidepoint(event.pos):
                        del points[1]
                        point_deleted = True   #only set to true if a point is deleted 
                if not point_deleted:
                    p= point.Point(event.pos[0], event.pos[1])
                    points.append(p)
                

        #display updates
        display.fill("white")

        for p in points:
            pygame.draw.circle(display, p.color, p.rect.center, p.rect.h / 2)


        #show display
        pygame.display.flip()

def main():
    pygame.init()
    display = pygame.display.set_mode()
    mainloop()

main()

# p2 = point.Point()

# p1.xcoor = 10

# print (p1.xcoor, p1.ycoor, p1.color, type(p1), id(p1) )
# print (p2.xcoor, p2.ycoor, p2.color, type(p2), id(p2) )

# points = []
# for p in range(10):
#     x = random.randint(0,250)
#     y = random.randint(0,2500)
#     points.append(point.Point(x,y))

# t = turtle.Turtle()
# for p in points:
#     p.random_color()
#     t.color(p.color)
#     t.goto(p.xcoor, p.ycoor)

# turtle.Screen().exitonclick()


# """
# t = turtle.Turtle()
# w = turtle.Turtle()
# #p1 = point.Point()  #p1 is an instance of Point, Point is a class
# p1.x = 10

# p1 = point.Point()  #p1 is an instance of Point, Point is a class
# p1.x = 5

# # state of p1(x=10, y=0, color="")
# # state of p2(x=5, y=0, color="")

# p1.color = "red"
# ## state of p1(x=10, y=0, color="red")
# point.Point()

# """

