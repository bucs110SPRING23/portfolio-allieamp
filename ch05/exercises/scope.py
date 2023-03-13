def main():
    def accum_mult(n):
        accumulator = start_number
        for i in range(n-1):
            accumulator = accumulator + start_number
        return accumulator
    def accum_exp(n):
        accumulator = start_number
        for i in range(n-1):
            accumulator = accumulator * start_number
        return accumulator
    def accum_square(n):
        accumulator = accum_exp(2)
        return accumulator 
    start_number = int(input("input start number:"))
    multiplier = int(input("input multiplier:"))
    multiplied = accum_mult(multiplier)
    exponized = accum_exp(multiplier)
    squared = accum_square(multiplier)
    print(multiplied)
    print(exponized)
    print(squared)
main()

