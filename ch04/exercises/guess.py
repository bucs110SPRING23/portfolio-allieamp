import random
number = int(random.randrange(1,1001))
guess = 0
guess_num = 0
print(number)
while guess != number:
    guess = int(input("Guess the number"))
    if guess == number:
        print("Correct!")
        break
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    guess_num = guess_num +1
print("The answer was:", number)
print("You took", guess_num, "tries")