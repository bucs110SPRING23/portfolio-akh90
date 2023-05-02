import pygame
from setup import *

class Enemy(pygame.sprite.Sprite):
    def __init__ (self, x, y):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('ch10\game\img\enemy.png')
        self.image = pygame.transform.scale(img, (tile_size, tile_size) )
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 
        self.move_direction = 1
        self.move_counter = 0
    def update(self):
        self.rect.x += self.move_direction
        self.move_counter += 1
        if abs(self.move_counter) > 15:
            self.move_direction *= -1
            self.move_counter *= -1

    
        




