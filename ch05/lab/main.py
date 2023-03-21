import pygame
pygame.init()

def threenp1(n):
    while n > 1.0:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return None

def threenp1range(upper_limit):
    values_dict = {}
    for n in range(2, upper_limit+1):
        y = 0
        threenp1(n)
        values_dict[n] = y
    return values_dict

def graph_coordinates(values_dict, screen, width, height):
    coordinates = []
    for n, y in values_dict.items():
        x = n
        coordinates.append((x*width//max(values_dict.keys()), height - y*height//max(values_dict.values())))
    if len(coordinates) > 1:
        pygame.draw.lines(screen, (255, 255, 255), False, coordinates)
    pygame.display.flip()

def main():
    
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))

    upper_limit = int(input("Enter upper limit: "))
    values_dictionary = threenp1range(upper_limit)

    graph_coordinates(values_dictionary, screen, width, height)
    pygame.display.set_caption(f"3n+1 Graph (Upper Limit: {upper_limit})")

    font = pygame.font.SysFont(None, 30)
    message = f"Value with maximum iterations: {max(values_dictionary, key=values_dictionary.get)} ({max(values_dictionary.values())} iterations)"
    text = font.render(message, True, (255, 255, 255))
    screen.blit(text, (10, 10))
    pygame.display.flip()
    

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

if __name__ == '__main__':
    main()


