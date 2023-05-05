import turtle
sides = int(input("Enter # of sides: "))
length = int(input("Enter side length: "))
franklin = turtle.Turtle()
franklin.shape("turtle")
franklin.color("pink")
for _ in range(sides):
    franklin.forward(length)
    franklin.right(360/sides)
window = turtle.Screen()
window.exitonclick()