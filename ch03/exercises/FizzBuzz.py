num = int(input("Enter an Upper Limit"))
for i in range(num+1):
    print("number:", i)
    if i % 5 == 0 and i % 3 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")