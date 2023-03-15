def accum_mult(x,y):
        accumulator = 0
        for _ in range(y):
            accumulator = accumulator + x
        return accumulator
def accum_exp(x,y):
    accumulator = 1
    for _ in range(y):
        accumulator = accumulator * x
    return accumulator
def accum_square(x):
    accumulator = accum_mult(x,x)
    return accumulator
def main():
     
    x = int(input("input x number:"))
    y = int(input("input y number:"))
    multiplied = accum_mult(x,y)
    exponized = accum_exp(x,y)
    squared = accum_square(x)
    print(multiplied)
    print(exponized)
    print(squared)
main()

