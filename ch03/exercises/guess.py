import random
number = int(random.randrange(1,11))
for i in range(3):
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