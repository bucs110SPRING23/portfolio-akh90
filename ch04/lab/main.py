import pygame
import random
import math 

pygame.init()
screen = pygame.display.set_mode()

dimensions = screen.get_size()
print (dimensions)
starting_point = [dimensions[0]-640, dimensions [1]-360]

screen.fill ("cornflowerblue")
pygame.display.flip()
pygame.time.wait (1000)

#circle
radius = 360
pygame.draw.circle(screen, "coral1", starting_point, radius)
pygame.draw.circle(screen, "black", starting_point, radius, width =3)
pygame.display.flip()
pygame.time.wait(500)

#hori_line
pygame.draw.line(screen, "black", ((dimensions[0]/2-360), (dimensions[1]/2)), ((dimensions[0]/2+360),(dimensions[1]/2)), width=2)
pygame.display.flip()


#vert_line
pygame.draw.line(screen, "black", ((dimensions[0]/2), (0)), ((dimensions[0]/2),(dimensions[1])), width=2)
pygame.display.flip()
pygame.time.wait(1000)

#part B
x1 = 640
y1 = 360
x2 = random.randrange (0,1280)
y2 = random.randrange (0,720)

distance_from_center = math.hypot(x2-x1, y2-y1)  #the distance formula
in_circle = distance_from_center <= dimensions[0]/2 #screen width

#pygame.draw.circle (screen, "black", (x2, y2), 3)

numdarts = 10
for i in range (numdarts):
    x1 = 640
    y1 = 360
    x2 = random.randrange (0,1280)
    y2 = random.randrange (0,720)
    dot = (x2,y2)

    if dot == in_circle:
        pygame.draw.circle (screen, "black", (x2, y2), 5)
    else:
        pygame.draw.circle (screen, "red", (x2, y2), 5)






pygame.display.flip()
pygame.time.wait(1000)