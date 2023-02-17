import random
import turtle 
import pygame
pygame.init()
import math

window = turtle.Screen()
jack = turtle.Turtle()
tina = turtle.Turtle()
jack.shape("turtle")
tina.shape("turtle")
jack.color("blue")
tina.color("purple")
jack.speed(2)
tina.speed(2)
jack.up()
tina.up()
jack.setpos(-100,20)
tina.setpos(-100,-20)
jack.down()
tina.down()
jack.forward(75)
tina.forward(75)
jack.setpos(-100,20)
tina.setpos(-100,-20)

jack.color("green")
tina.color("pink")
jack.up()
tina.up()
jack.setpos(-100,20)
tina.setpos(-100,-20)
jack.down()
tina.down()
for i in range(1,5,1):
    j = random.randrange(1,10)
    t = random.randrange(1,10)
    jack.forward(j)
    tina.forward(t)
jack.setpos(-100,20)
tina.setpos(-100,-20)
window.exitonclick()

window = pygame.display.set_mode()
points = []
side_length = int(50)
xpos = int(100)
ypos = int(100)
window.fill("white")
for s in [3,4,6,20,100,360]:
    for _ in [3,4,6,20,100,360]:
        angle = 360/s
        radians = math.radians(angle * 1)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
        pygame.display.flip()
    pygame.draw.polygon(window, "purple", points)
    pygame.display.flip()
    pygame.time.wait(1000)
    window.fill("pink")
    pygame.display.flip()
    points = []
