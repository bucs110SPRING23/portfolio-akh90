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
    pygame.time.wait (500)
    pygame.display.flip()
    screen.fill ("cornflowerblue")
   
