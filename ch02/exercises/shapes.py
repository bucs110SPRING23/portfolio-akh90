import pygame

pygame.init()

screen = pygame.display.set_mode() #full screen
#screen: variable
#pygame: modules that contain modules are called frameworks
#display: submodule of pygame
#set mode: funciton of the display module



screen.fill ("blue")
pygame.display.flip()
pygame.time.wait(1000)


#(x, y, width, height)
#dimensions = [100, 200, 250, 250]
#pygame.draw.rect(screen, "pink", dimensions) 

#dimensions = [10,10,0,30, 34]
pygame.draw.circle(screen, "white", [300,100], 50, 3) # (surface, color, center, radius, width)
pygame.draw.circle(screen, "white", [300, 270], 120, 3)
pygame.draw.circle(screen, "white", [300,550], 160, 3)



pygame.display.flip()
#input()
pygame.time.wait (2000)

