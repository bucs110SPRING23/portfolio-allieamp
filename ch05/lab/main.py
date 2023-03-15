import pygame
FACTOR = 30
def threenp1(n):
    count = 0
    while n > 1.0:
        count += 1
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = int(3 * n + 1)
    return count
def threenp1range(upper_limit):
    my_range = range(2,upper_limit+1)
    objs_in_sequence = {}
    for i, k in enumerate(my_range):
        threenp1(i)
        objs_in_sequence[k] = threenp1(k)            
    return objs_in_sequence
def graph_coordinates(result):
    coordinates = {}
    screen = pygame.display.set_mode()
    screen.fill("white")
    for k,v in result.items():
        coordinates[k*FACTOR] = v*FACTOR
    if len(result) >= 2:
        pygame.draw.lines(screen, "blue", True, list(coordinates.items()))
def maximum(upper_limit):
    max_so_far = 2
    for k,v in upper_limit.items():
        if v >= upper_limit[max_so_far]: 
            max_so_far = k
    return max_so_far
def main():
    pygame.init()
    screen = pygame.display.set_mode()
    screen.fill("white")
    upper_limit = int(10)
    result = threenp1range(upper_limit)
    print(result)

    graph_coordinates(result)
    width, height = screen.get_size()
    new_screen = pygame.transform.flip(screen, False, True)

    max_so_far = str(maximum(result))
    font = pygame.font.Font(None,48)
    msg = font.render(max_so_far, True, "blue")
    new_screen.blit(msg, (10,10))
    screen.blit(new_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(1000)

main()
