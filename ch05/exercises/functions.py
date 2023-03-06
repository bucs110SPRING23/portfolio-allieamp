def find_max(x,y,z):
    max = x
    if y > max:
        max = y
    if z> max:
        max = z
    print(max)

for _ in range(3):
    print("Please Enter 3 Numbers:")
    a = int(input(": "))
    b = int(input(": "))
    c = int(input(": "))
    find_max(a,b,c)

def foo(var):
    var +=1
    print(var)

var = 5
foo(var)
print(var)