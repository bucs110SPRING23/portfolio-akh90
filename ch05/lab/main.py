# import pygame
# pygame.init()

# def threenp1(n):
#     while n > 1.0:
#         if n % 2 == 0:
#             n = int(n / 2)
#         else:
#             n = int(3 * n + 1)
#     return None

# def threenp1range(upper_limit):
#     values_dict = {}
#     for n in range(2, upper_limit+1):
#         y = 0
#         threenp1(n)
#         values_dict[n] = y
#     return values_dict

# def graph_coordinates(values_dict, screen, width, height):
#     coordinates = []
#     for n, y in values_dict.items():
#         x = n
#         coordinates.append((x*width//max(values_dict.keys()), height - y*height//max(values_dict.values())))
#     if len(coordinates) > 1:
#         pygame.draw.lines(screen, (255, 255, 255), False, coordinates)
#     pygame.display.flip()

# def main():
    
#     width, height = 800, 600
#     screen = pygame.display.set_mode((width, height))

#     upper_limit = int(input("Enter upper limit: "))
#     values_dictionary = threenp1range(upper_limit)

#     graph_coordinates(values_dictionary, screen, width, height)
#     pygame.display.set_caption(f"3n+1 Graph (Upper Limit: {upper_limit})")

#     font = pygame.font.SysFont(None, 30)
#     message = f"Value with maximum iterations: {max(values_dictionary, key=values_dictionary.get)} ({max(values_dictionary.values())} iterations)"
#     text = font.render(message, True, (255, 255, 255))
#     screen.blit(text, (10, 10))
#     pygame.display.flip()
    

#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#     pygame.quit()

# if __name__ == '__main__':
#     main()


import pygame

def calculate_iterations(start, end):
    """
    Calculates the 3n+1 sequence for the given range [start, end] (inclusive),
    and stores the number of iterations for each value in a dictionary.
    Returns the dictionary.
    """
    iterations = {}
    for n in range(start, end+1):
        count = 0
        while n > 1:
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
            count += 1
        iterations[n] = count
    return iterations

def display_iterations(iterations):
    """
    Creates a display and uses a line graph to display the iterations
    for each value in the given dictionary. Prints the value with the max iterations
    on the graph.
    """
    pygame.init()
    font = pygame.font.SysFont('Arial', 20)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('3n+1 Sequence')
    screen.fill((255, 255, 255))
    pygame.draw.line(screen, (0, 0, 0), (50, 550), (750, 550), 2)
    pygame.draw.line(screen, (0, 0, 0), (50, 550), (50, 50), 2)
    max_n, max_count = max(iterations.items(), key=lambda x: x[1])
    max_label = font.render(f'Max iterations: {max_count} for n={max_n}', True, (0, 0, 255))
    screen.blit(max_label, (50, 20))
    x = 50
    for n, count in iterations.items():
        y = 550 - count * 5
        pygame.draw.circle(screen, (255, 0, 0), (x, y), 5)
        label = font.render(str(n), True, (0, 0, 0))
        screen.blit(label, (x-10, 560))
        x += 10
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

def main():
    iterations = calculate_iterations(1, 50)
    display_iterations(iterations)

if __name__ == '__main__':
    main()


