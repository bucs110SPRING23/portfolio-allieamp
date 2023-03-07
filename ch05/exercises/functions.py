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

def foo(var): #function scope uses var temporarily by does not change it fundamentaly
    var +=1 #using the same name as a globla variable called shadowing
    print(var)

var = 5
foo(var) #prints the var affected by the function foo
print(var) #prints the set var