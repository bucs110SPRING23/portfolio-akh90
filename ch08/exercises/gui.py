import pygame 
import pygame_menu

# class Player:
#     def __init__(self, pnum=1):
#         """
#         Initialize the player object
#         args: pnum [int] the player's id number
#         """
#         self.player_num = pnum
#         self.lives = 3 # players always start with 3 lives
#         self.is_large = False # player always starts small
#         self.coins = 0 #player starts with 0 coins

# class FloatingBrick:
#     def __init__(self, height, bnum):
#         """
#         Initializes the brick
#         args: type
#         """
#         self.bnum = bnum
#         self.is_solid = True
#         self.is_destroyable = False 
       
    

# class Mushroom:
#     def __init__(self, type):
#         """
#         Initializes the mushroom enemies
#         arg: type
#         """
#         self.type = type
#         self.speed = 1
#         self.is_dead = False

pygame.init()
screen = pygame.display.set_mode()

def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)


menu.mainloop(screen)