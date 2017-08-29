import random

highest = 10

anwer = random.randint(1, highest)

print("Please guess a number between 1 and {}".format(highest))
guess = int(input())

while guess != anwer:
    if guess == 0:
        print("Ok, better luck next time!")
        break
    
    if (guess < anwer):
        print("Please, guess higher!")
    else:
        print("Please, guess lower!")
    guess = int(input())
else:
    print("You got it!")
    