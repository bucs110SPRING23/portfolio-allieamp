import turtle
import random

franklin = turtle.Turtle()
franklin.shape("turtle")
franklin.color("pink")
franklin.speed(0)

window = turtle.Screen()
distance = 10
angle = 90
franklin.setpos(0,0)

is_in_screen = True
while is_in_screen:
    flip = random.randrange(0,2)
    if flip:
        franklin.right(angle)
    else:
        franklin.left(angle)
    franklin.forward(distance)
    turtleX = franklin.xcor()
    turtleY = franklin.ycor()

    x_range = window.window_width()/2
    y_range = window.window_height()/2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen == False

window.exitonclick()