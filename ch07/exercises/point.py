"""
does stuff 
"""
import random 
import pygame
from pygame import Rect


#blueprint for an object
#def graph_point():
#class == type
#class are names with TitleCase


#model is about how the class is used
class Point:
# docstring for Point #
    #functions are called methods when they are in a class 
    #first paramaeter to any method is 'self'
    def __init__(self, x=0, y=0): 
        #self ties the data to the objects scope
        self.on = True
        self.rect = pygame.Rect(abs(x), abs(y), size, size)

        self.color = self.random_color()
        self.radius = 5

    def random_color (self):
        return (random.randint(0,255,),random.randint(0,255,),random.randint(0,255,) )
       # self.color = ("red", "green", "blue", "yellow", "orange", "purple")

    

