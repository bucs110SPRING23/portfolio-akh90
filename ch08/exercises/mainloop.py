import pygame
import turtle

def mainloop():
    display = pygame.display.set_mode()
    points = []
    #mainloop
    while True:
        #eventloop
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                point_deleted = False
                for i, p in enumerate(points):
                    if p.rect.collidepoint(event.pos):
                        del points[i]
                        point_deleted = True
                        
                
