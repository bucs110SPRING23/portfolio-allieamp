import random
import math
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))

screen.fill("lightblue")
pygame.display.flip()
pygame.draw.circle(screen,"black",(250,250),250)
pygame.draw.circle(screen,"purple",(250,250),245)            
pygame.display.flip()            
pygame.draw.line(screen,"black",(250,0),(250,500))
pygame.draw.line(screen,"black",(0,250),(500,250))
pygame.display.flip()
pygame.time.wait(2000)

for _ in range(10):
    x_dart = random.randrange(0,500)
    y_dart = random.randrange(0,500)
    distance_from_center = math.hypot(250-x_dart, 250-y_dart) #the distance formula
    is_in_circle = distance_from_center <= 500/2 #screen width
    if is_in_circle == True:
        pygame.draw.circle(screen,"green",(x_dart,y_dart),5)
    elif is_in_circle == False:
        pygame.draw.circle(screen,"red",(x_dart,y_dart),5)
    pygame.display.flip()
    pygame.time.wait(1000)
pygame.time.wait(3000)
    
