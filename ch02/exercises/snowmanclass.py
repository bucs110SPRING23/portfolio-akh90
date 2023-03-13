import pygame

pygame.init()


screen = pygame.display.set_mode()

dimensions = screen.get_size()
print (dimensions)
starting_point = [dimensions[0] // 2, dimensions [1] // 2 -300]

radius = 20
for _ in range (3):
    pygame.draw.circle(screen, "red", starting_point, radius)
    starting_point [1] = starting_point[1] - radius
    radius  = radius // 2
    starting_point [1] = starting_point[1] - radius


pygame.display.flip()
pygame.time.wait(2000)
    