import pygame
import random
import math 

#set up screen
pygame.init()
screen = pygame.display.set_mode()

dimensions = screen.get_size()
print (dimensions)
starting_point = [dimensions[0]-640, dimensions [1]-360]

screen.fill ("cornflowerblue")
pygame.display.flip()
pygame.time.wait (1000)

font = pygame.font.SysFont(None, 30)
#set up player colors
player1_color = (255, 0, 0)  # Red
player2_color = (0, 0, 255)  # Blue

#drawing the player boxes 
player1_box = pygame.Rect(100, 100, 100, 100)
player2_box = pygame.Rect(600, 100, 100, 100)
pygame.draw.rect(screen, player1_color, player1_box)
pygame.draw.rect(screen, player2_color, player2_box)

# Display text prompt
text = font.render("Who do you think will win?", True, (0, 0, 0))
text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
screen.blit(text, text_rect)

pygame.display.flip()


# user selects a player
player_selected = None
while not player_selected:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player1_box.collidepoint(event.pos):
                player_selected = 1
            elif player2_box.collidepoint(event.pos):
                player_selected = 2

#pygame.display.flip()
screen.fill ("cornflowerblue") 

#circle
radius = 360
pygame.draw.circle(screen, "coral1", starting_point, radius)
pygame.draw.circle(screen, "black", starting_point, radius, width =3)
pygame.display.flip()
pygame.time.wait(500)

#hori_line
pygame.draw.line(screen, "black", ((dimensions[0]/2-360), (dimensions[1]/2)), ((dimensions[0]/2+360),(dimensions[1]/2)), width=2)
pygame.display.flip()


#vert_line
pygame.draw.line(screen, "black", ((dimensions[0]/2), (0)), ((dimensions[0]/2),(dimensions[1])), width=2)
pygame.display.flip()
pygame.time.wait(1000)


# Start the dart game
center = (screen.get_width() // 2, screen.get_height() // 2)
num_rounds = 5
player1_score = 0
player2_score = 0
for i in range(num_rounds):
    # Player 1's turn
    x1 = center[0] - 360
    y1 = center[1]
    x2 = random.randrange(0, screen.get_width())
    y2 = random.randrange(0, screen.get_height())
    distance_from_center = math.hypot(x2 - center[0], y2 - center[1])
    in_circle = distance_from_center <= 360
    if in_circle:
        player1_score += 1
        color = player1_color
    else:
        color = (0, 0, 0)
    pygame.draw.circle(screen, color, (x2, y2), 10)
    pygame.display.update()

    # Player 2's turn
    x1 = center[0] + 360
    y1 = center[1]
    x2 = random.randrange(0, screen.get_width())
    y2 = random.randrange(0, screen.get_height())
    distance_from_center = math.hypot(x2 - center[0], y2 - center[1])
    in_circle = distance_from_center <= 360
    if in_circle:
        player2_score += 1
        color = player2_color
    else:
        color = (0, 0, 0)
    pygame.draw.circle(screen, color, (x2, y2), 10)
    pygame.display.update()
    pygame.time.wait(4000)

screen.fill ("cornflowerblue")
#winner nd loser
if player1_score > player2_score:
    winner = "Player 1 wins!"
    if player_selected == 1:
        guess_result = "You guessed correctly!"
    else:
        guess_result = "You guessed wrong!"
elif player2_score > player1_score:
    winner = "Player 2 wins!"
    if player_selected == 2:
        guess_result = "You guessed correctly!"
    else:
        guess_result = "You guessed wrong!"

text = font.render( winner, True, (0, 0, 0))
text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
screen.blit(text, text_rect)

pygame.display.flip()
pygame.time.wait(2000)

screen.fill ("cornflowerblue")

text = font.render(guess_result, True, (0, 0, 0))
text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
screen.blit(text, text_rect)

pygame.display.flip()
pygame.time.wait(2000)

screen.fill ("cornflowerblue")

text = font.render("thank you for playing :}", True, (0, 0, 0))
text_rect = text.get_rect(center=(screen.get_width() // 2, 50))
screen.blit(text, text_rect)

pygame.display.flip()
pygame.time.wait(2000)