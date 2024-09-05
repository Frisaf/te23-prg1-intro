import random

guess = False
answer = random.randint(1, 10)

while answer != guess:
    try:
        guess = int(input("Guess a number between 1 and 100: "))

        if guess > answer:
            print("You guessed too high!")
            
        elif guess < answer:
            print("You guessed too low.")
        
        elif answer == guess:
            print(f"You won! The number was {answer}")
    
    except ValueError:
        print("That is not a number.")