import turtle
sides = int(input("Enter # of sides"))
length = float(input("Enter side length"))
franklin = turtle.Turtle()
franklin.shape("turtle")
franklin.color("red")
for _ in range(sides):
    franklin.forward(length)
    franklin.right(360/sides)
window = turtle.Screen()
window.exitonclick()