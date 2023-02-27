import random
import math
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

screen.fill("blue")
pygame.display.flip()
pygame.draw.circle(screen,"lightblue",(250,250),250)            
pygame.display.flip()            
pygame.draw.line(screen,"black",(250,0),(250,500))
pygame.draw.line(screen,"black",(0,250),(500,250))
pygame.display.flip()
pygame.time.wait(2000)

player1_score = int(0)
player2_score = int(0)
for _ in range(10):
    x_dart = random.randrange(0,500)
    y_dart = random.randrange(0,500)
    distance_from_center = math.hypot(250-x_dart, 250-y_dart)
    is_in_circle = distance_from_center <= 500/2
    if is_in_circle == True:
        pygame.draw.circle(screen,"green",(x_dart,y_dart),5)
        player1_score = player1_score + 1
    elif is_in_circle == False:
        pygame.draw.circle(screen,"red",(x_dart,y_dart),5)
    pygame.display.flip()
    x_dart = random.randrange(0,500)
    y_dart = random.randrange(0,500)
    distance_from_center = math.hypot(250-x_dart, 250-y_dart)
    is_in_circle = distance_from_center <= 500/2
    if is_in_circle == True:
        pygame.draw.circle(screen,"purple",(x_dart,y_dart),5)
        player2_score = player2_score + 1
    elif is_in_circle == False:
        pygame.draw.circle(screen,"pink",(x_dart,y_dart),5)
    pygame.display.flip()
    pygame.time.wait(500)


print(player1_score, player2_score)
if player1_score > player2_score:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 1 Wins!", True, "white")
    screen.blit(text, (250, 250))
elif player1_score < player2_score:
    font = pygame.font.Font(None, 48)
    text = font.render("Player 2 Wins!", True, "white")
    screen.blit(text, (250, 250))
else:
    font = pygame.font.Font(None, 48)
    text = font.render("Tie!", True, "white")
    screen.blit(text, (250, 250))
pygame.display.flip()
pygame.time.wait(1000)
