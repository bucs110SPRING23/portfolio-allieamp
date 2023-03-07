import random
import math
import pygame
pygame.init()
screen = pygame.display.set_mode()
(width, height) = pygame.display.get_window_size()

hitbox_width = int(width / 2)
hitbox_height = int(height / 2)

screen.fill("black")
hitboxes = {
    "Player1": pygame.Rect(0,100,hitbox_width,hitbox_height),
    "Player2": pygame.Rect(hitbox_width+20,100,hitbox_width,hitbox_height),
}
box_colors = {
    "Player1":(0,100,0),
    "Player2":(100,0,100),
}

highlight_colors = {
    "Player1":(0,200,0),
    "Player2":(200,0,200),
}

font = pygame.font.Font(None, 48)
text = font.render("Choose Who Will Win", True, "white")
screen.blit(text, (100,50))
pygame.draw.rect(screen,box_colors["Player1"],hitboxes["Player1"])
pygame.draw.rect(screen,box_colors["Player2"],hitboxes["Player2"])
text1 = font.render("Player 1", True, "white")
screen.blit(text1, hitboxes["Player1"])
text2 = font.render("Player 2", True, "white")
screen.blit(text2, hitboxes["Player2"])
pygame.display.flip()

bet = []
done = False

while not done: 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["Player1"].collidepoint(event.pos):
                bet.append("Player 1")
                pygame.draw.rect(screen,highlight_colors["Player1"],hitboxes["Player1"])
                pygame.display.flip()
                pygame.time.delay(500)
                done = True
            elif hitboxes["Player2"].collidepoint(event.pos):
                bet.append("Player 2")
                pygame.draw.rect(screen,highlight_colors["Player2"],hitboxes["Player2"])
                pygame.display.flip()
                pygame.time.delay(500)
                done = True


screen.fill("black")
pygame.display.flip()
pygame.draw.circle(screen,"white",(hitbox_width,hitbox_height),hitbox_height)  
pygame.draw.circle(screen,"blue",(hitbox_width,hitbox_height),hitbox_height-5)
pygame.draw.circle(screen,"lightblue",(hitbox_width,hitbox_height),hitbox_height-50)
pygame.draw.circle(screen,"blue",(hitbox_width,hitbox_height),hitbox_height-100)
pygame.draw.circle(screen,"lightblue",(hitbox_width,hitbox_height),hitbox_height-150)
pygame.draw.circle(screen,"blue",(hitbox_width,hitbox_height),hitbox_height-200)
pygame.draw.circle(screen,"lightblue",(hitbox_width,hitbox_height),hitbox_height-250)
pygame.draw.circle(screen,"red",(hitbox_width,hitbox_height),hitbox_height-300)                        
pygame.display.flip()            
pygame.draw.line(screen,"black",(hitbox_width,0),(hitbox_width,height))
pygame.draw.line(screen,"black",(0,hitbox_height),(width,hitbox_height))
pygame.display.flip()

player1_score = int(0)
player2_score = int(0)
for _ in range(10):
    x_dart = random.randrange(0,width)
    y_dart = random.randrange(0,height)
    distance_from_center = math.hypot(hitbox_width-x_dart, hitbox_height-y_dart)
    is_in_circle = distance_from_center <= hitbox_height
    if is_in_circle == True:
        pygame.draw.circle(screen,"green",(x_dart,y_dart),5)
        player1_score = player1_score + 1
    elif is_in_circle == False:
        pygame.draw.circle(screen,"red",(x_dart,y_dart),5)
    pygame.display.flip()
    pygame.time.wait(500)
    x_dart = random.randrange(0,width)
    y_dart = random.randrange(0,height)
    distance_from_center = math.hypot(hitbox_width-x_dart, hitbox_height-y_dart)
    is_in_circle = distance_from_center <= hitbox_height
    if is_in_circle == True:
        pygame.draw.circle(screen,"purple",(x_dart,y_dart),5)
        player2_score = player2_score + 1
    elif is_in_circle == False:
        pygame.draw.circle(screen,"pink",(x_dart,y_dart),5)
    pygame.display.flip()
    pygame.time.wait(500)


if player1_score > player2_score:
    winner = ["Player 1"]
    font = pygame.font.Font(None, 48)
    text = font.render("Player 1 Wins!", True, "white")
    screen.blit(text, (hitbox_width, hitbox_height))
elif player1_score < player2_score:
    winner = ["Player 2"]
    font = pygame.font.Font(None, 48)
    text = font.render("Player 2 Wins!", True, "white")
    screen.blit(text, (hitbox_width, hitbox_height))
else:
    winner = ["No one"]
    font = pygame.font.Font(None, 48)
    text = font.render("Tie!", True, "white")
    screen.blit(text, (hitbox_width, hitbox_height))
if bet == winner:
    font = pygame.font.Font(None, 48)
    text = font.render("You Guessed Right", True, "white")
    screen.blit(text, (hitbox_width, hitbox_height+100))
else:
    font = pygame.font.Font(None, 48)
    text = font.render("You Guessed Wrong", True, "white")
    screen.blit(text, (hitbox_width, hitbox_height+100))
pygame.display.flip()
pygame.time.wait(1000)
print(bet == winner)
