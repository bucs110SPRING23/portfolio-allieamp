def star_pyramid(rows):
    for i in range(1,rows+1):
        print("*" * i) 


def rstar_pyramid(rows):
    for i in range(rows,0,-1):
        print("*" * i) 
rows = int((input("Set number of rows:")))
star_pyramid(rows)
rstar_pyramid(rows)
