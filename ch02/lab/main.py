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
jack.speed(1)
tina.speed(1)
jack.up()
tina.up()
jack.setpos(-100,20)
tina.setpos(-100,-20)
jack.down()
tina.down()
jack.forward(20)
tina.forward(20)
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
for i in range(1,10,1):
    j = random.randrange(1,10)
    t = random.randrange(1,10)
    jack.forward(j)
    tina.forward(t)
jack.setpos(-100,20)
tina.setpos(-100,-20)
window.exitonclick()

num_sides = int(3)
window = pygame.display.set_mode()
side_length = int(50)
xpos = int(100)
ypos = int(100)
window.fill("pink")

pygame.display.flip()
for num_sides in [3,4,6,20,100,360]:
    points = []
    print(num_sides)
    for i in range(0,num_sides,1):
        angle = 360/num_sides
        radians = math.radians(angle * i)
        x = xpos + side_length * math.cos(radians)
        y = ypos + side_length * math.sin(radians)
        points.append([x,y])
    print(num_sides)
    pygame.draw.polygon(window, "black", points)
    pygame.display.flip()
    pygame.time.wait(5000)
    window.fill("pink")
    pygame.display.flip()
