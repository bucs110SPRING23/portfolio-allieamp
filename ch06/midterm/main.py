import turtle

def angle(sides=6):
    """
    Calculates angle based on # sides of shape
    args:(int) # sides in shape
    return: (int) internal angle of shape
    """
    angle = 360/sides
    return angle  

def main():
    #setting up turtle
    franklin = turtle.Turtle()
    franklin.shape("turtle")
    franklin.pensize(8)
    franklin.speed(8)
    franklin.color("black")
    hexangle = angle(sides=6)
    length = 60
    
    #drawing circle
    for _ in range(40):
        circangle = angle(sides=40)
        franklin.forward(length/12)
        franklin.right(circangle)
    
    #shifting up to draw hexagon
    franklin.up()
    franklin.left(90)
    franklin.forward(length/2)
    franklin.right(hexangle)
    franklin.down()

    #drawing hexagon
    for _ in range(6):
        franklin.right(hexangle)
        franklin.forward(length)

    #shifting to carbon for alcohol group
    franklin.up()
    franklin.right(180)
    franklin.forward(length)
    franklin.right(hexangle)
    franklin.down()

    #drawing top alcohol group
    franklin.forward(length/2)
    franklin.color("red")
    franklin.forward(length/2)
    franklin.color("gray")
    franklin.right(45)
    franklin.forward(length/4)
 
    #retreating from alcohol group
    franklin.up()
    franklin.color("black")
    franklin.right(180)
    franklin.forward(length/4)
    franklin.left(45)
    franklin.forward(length)
    franklin.right(hexangle)

    #shift to next carbon
    franklin.forward(length)
    franklin.right(hexangle)
    franklin.down()

    #drawing bottom alcohol group
    franklin.forward(length/2)
    franklin.color("red")
    franklin.forward(length/2)
    franklin.color("gray")
    franklin.left(45)
    franklin.forward(length/4)

    #retreating from bottom alcohol group
    franklin.up()
    franklin.color("black")
    franklin.right(180)
    franklin.forward(length/4)
    franklin.right(45)
    franklin.forward(length)
    franklin.right(hexangle)
    
    #shifting to amide carbon
    for _ in range(3):
        franklin.forward(length)
        franklin.left(hexangle)

    #drawing amide group
    franklin.right(hexangle*2)
    franklin.down()
    franklin.forward(length)
    franklin.right(hexangle)
    franklin.forward(length)
    franklin.left(hexangle)
    franklin.forward(length/2)
    franklin.color("blue")
    franklin.forward(length/2)
    franklin.right(45)
    franklin.color("gray")
    franklin.forward(length/4)
    franklin.right(180)
    franklin.forward(length/4)
    franklin.right(45)
    franklin.forward(length/4)


    window = turtle.Screen()
    window.exitonclick()

main()