import pygame

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode() #full screen
#screen: variable
#pygame: modules that contain modules are called frameworks
#display: submodule of pygame
#set mode: funciton of the display module


screen.fill ("purple")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill ("blue")
pygame.display.flip()
pygame.time.wait(1000)
screen.fill ("green")
pygame.display.flip()
pygame.time.wait(1000)
#pygame.time.Clock

#(x, y, width, height)
dimensions = [100, 200, 250, 250]
pygame.draw.rect(screen, "pink", dimensions) 

dimensions = [100,250,10,10]
pygame.draw.rect(screen, "black", dimensions) #(x, y, width, height)

dimensions = [300,250,10,10]
pygame.draw.rect(screen, "black", dimensions) #(x, y, width, height)

dimensions = [(200, 350), (300,350)]
pygame.draw.lines(screen, "black", True, dimensions, width = 10)

my_font = pygame.font.SysFont('Comic Sans MS', 30)
text1 = my_font.render('k*ll me now', True, (0,0,255))
screen.blit(text1, (100,100))



pygame.display.flip()
#input()
pygame.time.wait (6000)