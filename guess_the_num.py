# Guess the number
import random

# cpu will think of a random number b/w 1 to 100
cpu = random.randint(1,100)

# user will have only 5 chances
game = True
while game:
    guess = int(input("Enter your guess : "))
    if cpu == guess:
        print("You have guessed the number...")
        break
    elif cpu > guess:
        print("You have guessed a smaller number...")
    elif cpu < guess:
        print("You have guessed a greater number...")
