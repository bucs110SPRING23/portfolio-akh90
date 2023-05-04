import pygame
from os import path
import pickle

from player import Player
from world import World
from button import Button
from coin import Coin
from exit import Exit
from enemy import Enemy
from platform import Platform

# Define colours
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

class Controller:
    def __init__(self):
        pygame.init()

        # Create screen
        self.screen_width = 1000
        self.screen_height = 1000
        self.screen = pygame.display.set_mode(size=(self.screen_width, self.screen_height))
        self.width, self.height = pygame.display.get_window_size()

        # Set clock
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Set default font
        self.font = pygame.font.SysFont('Bauhaus 93', 70)
        self.font_score = pygame.font.SysFont('Bauhaus 93', 30)


        # Define game variables
        self.tile_size = 50
        self.game_over = 0
        self.level = 1
        self.max_levels = 7
        self.score = 0
        self.main_menu = True

        # Load in level data and create world
        if path.exists(f'ch10/game/levels/level{self.level}_data'):
            pickle_in = open(f'ch10/game/levels/level{self.level}_data', 'rb')
            world_data = pickle.load(pickle_in)
        self.world = World(world_data, self.tile_size)

        # Load a player
        self.player = Player(100, self.screen_height - 130)

        # Create empty sprite groups for all models you need to draw
        self.blob_group = pygame.sprite.Group()
        self.platform_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()

        #create dummy coin for showing the score
        score_coin = Coin(self.tile_size // 2, self.tile_size // 2)
        self.coin_group.add(score_coin)


        #load sounds
        pygame.mixer.music.load('ch10/game/sounds/music.wav')
        pygame.mixer.music.play(-1, 0.0, 5000)
        self.coin_fx = pygame.mixer.Sound('ch10/game/sounds/img_coin.wav')
        self.coin_fx.set_volume(0.5)
        self.jump_fx = pygame.mixer.Sound('ch10/game/sounds/img_jump.wav')
        self.jump_fx.set_volume(0.5)
        self.game_over_fx = pygame.mixer.Sound('ch10/game/sounds/img_game_over.wav')
        self.game_over_fx.set_volume(0.5)

        # Create buttons
        start_img = pygame.image.load('ch10/game/img/start_btn.png')
        exit_img = pygame.image.load('ch10/game/img/exit_btn.png')
        restart_img = pygame.image.load('ch10/game/img/restart_btn.png')
        self.start_button = Button(self.screen_width // 2 - 350, self.screen_height // 2, start_img)
        self.exit_button = Button(self.screen_width // 2 + 150, self.screen_height // 2, exit_img)
        self.restart_button = Button(self.screen_width // 2 - 50, self.screen_height // 2 + 100, restart_img)


    def game_loop(self):
        # You are in the game loop, so you need to check for the following events:
        # This function should manage all the events that occur in the game loop.
        # You need to check for the following events:
        # 1. Quit event
        # 2. Keydown event to move the player and jump
        # 3. Keyup event to stop the player from moving
        # 4. Collision with coins
        # 5. Collision with exit
        # 6. Collision with platforms
        # 7. Collision with lava
        # 8. Collision with enemies
        # 9. Collision with world boundaries
        while self.state == "GAME":
            self.world.draw()

            if game_over == 0:
                self.blob_group.update()
                self.platform_group.update()
                #update score
                #check if a coin has been collected
                if pygame.sprite.spritecollide(self.player, self.coin_group, True):
                    self.score += 1
                    self.coin_fx.play()
                self.draw_text('X ' + str(self.score), self.font_score, WHITE, self.tile_size - 10, 10)

            self.blob_group.draw(self.screen)
            self.platform_group.draw(self.screen)
            self.lava_group.draw(self.screen)
            self.coin_group.draw(self.screen)
            self.exit_group.draw(self.screen)

            game_over = self.player.update(game_over)

            #if player has died
            if game_over == -1:
                if self.restart_button.draw():
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                    #score = 0
                    self.game_over_fx.stop()
                    pygame.mixer.music.load('ch10/game/sounds/music.wav')
                    pygame.mixer.music.play(-1, 0.0, 5000)


            #if player has completed the level
            if game_over == 1:
                #reset game and go to next level
                level += 1
                if level <= max_levels:
                    #reset level
                    world_data = []
                    world = reset_level(level)
                    game_over = 0
                else:
                    draw_text('YOU WIN!', font, blue, (screen_width // 2) - 140, screen_height // 2)
                    if restart_button.draw():
                        level = 1
                        #reset level
                        world_data = []
                        world = reset_level(level)
                        game_over = 0
                        #score = 0


    def start_menu(self):
        """
        Display a start menu for the game.
        """
        sun_img = pygame.image.load('ch10/game/img/sun.png')
        bg_img = pygame.image.load('ch10/game/img/sky.png')

        self.clock.tick(self.fps)
        self.screen.blit(bg_img, (0, 0))
        self.screen.blit(sun_img, (100, 100))

        # Check for events
        # You are at the start menu, so you only need to check for the mouse click
        # on the start button or the exit button.
        # If the start button is clicked, call the start_game() method.
        # If the exit button is clicked, set the state to "QUIT" to exit the game.
        while self.state == "START":
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.rect.collidepoint(event.pos):
                        self.start_game()
                    elif exit_button.rect.collidepoint(event.pos):
                        self.state = "QUIT"

            start_button.draw(self.screen)
            exit_button.draw(self.screen)

            pygame.display.flip()


    def mainloop(self):
        """
        Main loop for the game.
        """
        self.state = "START"
        while True:
            if self.state == "START":
                self.start_menu()
            elif self.state == "GAME":
                self.game_loop()
            elif self.state == "QUIT":
                pygame.quit()
                exit()


    def start_game(self):
        self.state = "GAME"


    def draw_text(self, text, text_col, x, y):
        """
        Draw text onto the screen.

        Args:
            text (_type_): a text string
            text_col (_type_): a colour
            x (_type_): position on the x-axis
            y (_type_): position on the y-axis
        """
        img = self.font.render(text, True, text_col)
        self.screen.blit(img, (x, y))