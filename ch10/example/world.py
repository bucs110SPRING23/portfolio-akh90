import pygame
from pygame.locals import *
from pygame import mixer
from enemy import Enemy
from platform import Platform
from lava import Lava
from coin import Coin
from exit import Exit


class World():
	def __init__(self, data, tile_size, blob_group, platform_group, lava_group, coin_group, exit_group):
		self.tile_list = []

		#load images
		dirt_img = pygame.image.load('ch10/game/img/dirt (1).png')
		grass_img = pygame.image.load('ch10/game/img/grass (1).png')

		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 1:
					img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					img = pygame.transform.scale(grass_img, (tile_size, tile_size))
					img_rect = img.get_rect()
					img_rect.x = col_count * tile_size
					img_rect.y = row_count * tile_size
					tile = (img, img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					blob = Enemy(col_count * tile_size, row_count * tile_size + 15)
					blob_group.add(blob)
				if tile == 4:
					platform = Platform(col_count * tile_size, row_count * tile_size, 1, 0, tile_size)
					platform_group.add(platform)
				if tile == 5:
					platform = Platform(col_count * tile_size, row_count * tile_size, 0, 1, tile_size)
					platform_group.add(platform)
				if tile == 6:
					lava = Lava(col_count * tile_size, row_count * tile_size + (tile_size // 2), tile_size)
					lava_group.add(lava)
				if tile == 7:
					coin = Coin(col_count * tile_size + (tile_size // 2), row_count * tile_size + (tile_size // 2), tile_size)
					coin_group.add(coin)
				if tile == 8:
					exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2), tile_size)
					exit_group.add(exit)
				col_count += 1
			row_count += 1


	def draw(self, screen):
		for tile in self.tile_list:
			screen.blit(tile[0], tile[1])
