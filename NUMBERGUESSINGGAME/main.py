# Importing Library 
import random as randomlib

print("Guess a number between 1 and 1000")

while True: # Entering the loop
    random = randomlib.randint(1, 1000) # Defining Range

    guess = int(input("Enter Number: ")) # Input for Guess

    if guess < random:
        print("Too low")
    elif guess > random:
        print("Too high")
    else:
        print("That's right!")
        break