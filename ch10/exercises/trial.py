import pygame

# initialize pygame
pygame.init()

# set up the game window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mario")

# define some colors
black = (0, 0, 0)
white = (255, 255, 255)

#graphics 
background_image = pygame.image.load ("background.jpg")
mario_image = pygame.image.load ("mario.png")

#set up the ground


# set up the player
player_image = pygame.image.load("mario.png")
player_rect = player_image.get_rect()
player_rect.x = 100
player_rect.y = 500

# set up the ground
ground_rect = pygame.Rect(0, 550, 800, 50)

# define the game loop
running = True
while running:

    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_SPACE]:
        player_rect.y -= 10

    # check for collisions with the ground
    if player_rect.colliderect(ground_rect):
        player_rect.bottom = ground_rect.top

    # draw the screen
    screen.fill(black)
    pygame.draw.rect(screen, white, ground_rect)
    screen.blit(player_image, player_rect)
    pygame.display.flip()

# clean up
pygame.quit()
