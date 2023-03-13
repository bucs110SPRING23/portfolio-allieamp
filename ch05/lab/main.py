import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode()
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
    upper_limit = int(input("Set upper limit:"))
    result = threenp1range(upper_limit)
    print(result)
    
    def graph_coordinates(result):
        coordinates = [result]
        pygame.draw.lines(screen, "blue", True, coordinates)
    graph_coordinates(result)
    new_screen = pygame.transform.flip(screen, False, True)
    width, height = new_screen.get_size()
    new_screen = pygame.transform.scale(new_screen, (width * 5, height * 5))
    screen.blit(new_screen, (0, 0))
    max_so_far = 0 
    if threenp1() > max_so_far:
        max_so_far = threenp1()
    else: 
        max_so_far = max_so_far
    font = pygame.font.Font(None,48)
    msg = font.render(max_so_far, True, "blue")
    screen.blit(msg, (10,10))
    pygame.display.flip()
    pygame.time.delay(1000)

main()
