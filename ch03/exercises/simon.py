import pygame
pygame.init()
import random
screen = pygame.display.set_mode()
colors = ["red", "green", "blue", "yellow"]
random.shuffle(colors)
for color in colors:
  screen.fill(color)
  pygame.display.flip()
  pygame.time.wait(500)

  #add black screen between each color to make them more distinct
  screen.fill("black")
  pygame.display.flip()
  pygame.time.wait(250)
msg = """
Simon Says:
  UP: red
  DOWN: blue
  LEFT: green
  RIGHT: yellow

  Click on the window, enter the sequence, then press <enter>
"""
response = input(msg) # use input to pause the program for the user

user_guess = []
for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
    if(event.key == pygame.K_UP):
      screen.fill("red")
      user_guess.append("red")
    elif(event.key == pygame.K_DOWN):
      screen.fill("blue")
      user_guess.append("blue")
    elif(event.key == pygame.K_LEFT):
      screen.fill("green")
      user_guess.append("green")
    elif(event.key == pygame.K_RIGHT):
      screen.fill("yellow")
      user_guess.append("yellow")
    pygame.display.flip()
    pygame.time.wait(1000)

print("You Entered:", user_guess)
print("The correct pattern was", colors)

if user_guess == colors:
  print("Correct! You win.")
else:
  print("Were you even paying attention?")

pygame.quit()