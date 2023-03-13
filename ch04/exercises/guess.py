import random
number = int(random.randrange(1,1001))
guess = 0
guess_num = 0
while guess != number:
    guess = int(input("Guess the number"))
    guess_num = guess_num +1
    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
print("The answer was:", number)
print("You took", guess_num, "tries")