import pygame
pygame.init()
screen = pygame.display.set_mode()
screen.fill("blue")
pygame.display.flip()
pygame.time.wait(1000)
pygame.draw.circle(screen, "white", [650,525], 150)
pygame.draw.circle(screen, "white", [650,325], 100)
pygame.draw.circle(screen, "white", [650,200], 50)
pygame.display.flip()
pygame.time.wait(1000)

for i in range(100, 1500, 100):
    pygame.draw.circle(screen, "white", [100,i], 15)
pygame.display.flip()
pygame.time.wait(1000)
for i in range(100, 1000, 100):
    pygame.draw.circle(screen, "blue", [100,i], 15)
    pygame.draw.circle(screen, "white", [100,i+25], 15)
    pygame.display.flip()
    pygame.time.wait(500)
pygame.display.flip()
pygame.time.wait(1000)