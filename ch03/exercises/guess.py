import random
number = int(random.randrange(1,11,1))
for i in range(1,4,1):
    guess = int(input("Guess the number"))
    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
if guess != number:
    print("Wrong!")
print("The answer was:", number)