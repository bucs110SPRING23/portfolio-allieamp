import pygame
pygame.init()
screen = pygame.display.set_mode()

screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)
pygame.draw.circle(screen, "black", [650,525], 155)
pygame.draw.circle(screen, "black", [650,325], 105)
pygame.draw.circle(screen, "black", [650,200], 55)
pygame.draw.circle(screen, "white", [650,525], 150)
pygame.draw.circle(screen, "white", [650,325], 100)
pygame.draw.circle(screen, "white", [650,200], 50)
pygame.display.flip()
pygame.time.wait(1000)

for _ in range (0, 1500, 100):
    for i in range(0, 1500, 100):
        pygame.draw.circle(screen, "white", [_,i], 15)
pygame.display.flip()
for _ in range (0, 1500, 100):
    pygame.display.flip()
    for i in range(0, 1500, 100):
        pygame.draw.circle(screen, "blue", [_,i], 15)
        pygame.draw.circle(screen, "white", [_,i+25], 15)
        pygame.display.flip()
        pygame.time.wait(25)
pygame.display.flip()
pygame.time.wait(500)

