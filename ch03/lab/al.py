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
pygame.draw.polygon (screen, "black", [[700,200],[700, 300] , [550,300], [550,200]])

#for _ in range (3):
#    angle = 360/num_sides


pygame.display.flip()
pygame.time.wait (1000)