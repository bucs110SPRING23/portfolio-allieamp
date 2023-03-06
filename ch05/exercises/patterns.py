def star_pyramid():
    rows = int((input("Set number of rows:")))
    for i in range(1,rows+1):
        print("*" * i) 
star_pyramid()

def rstar_pyramid():
    rows = int((input("Set number of rows:")))
    for i in range(rows+1,1,-1):
        print("*" * i) 
rstar_pyramid()
