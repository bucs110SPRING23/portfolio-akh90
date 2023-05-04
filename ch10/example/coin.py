import pygame


class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y, tile_size):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('ch10/game/img/coin.png')
		self.image = pygame.transform.scale(img, (tile_size, tile_size)) # // 2, tile_size // 2))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)