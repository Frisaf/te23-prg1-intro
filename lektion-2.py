print("Hello and welcome to my program") # Use print to print a greeting in the terminal

user_name = input("What's your name?\n> ") # Use the built in function input to ask for the user's name.
print(f"Hello {user_name}! So unpleasant to meet you =^v^=") # Use an f string to format print and print a greeting with the user's name

print("I wonder how ancient you are... (or how much of a baby)")

try:
    while True:
        user_age = float(input("What's your age: "))

        if user_age <= 1:
            print("Are you reallyone year or younger?")

        elif user_age <= 0:
            print("You can't be zero years old or younger... idiot.")

        elif user_age >= 100:
            print("WOW you're ancient for real.")
            break

        elif user_age >= 50:
            print("OLD!!! \U0001F480 \U0001F480 \U0001F480")
            break
        
        elif user_age < 13:
            print("BABY!!! \U0001F923")
            break

        else:
            print(f"Okay! That means that you will be {user_age + 1:.0f} years old next year! One step closer to the grave \U0001F970")
            break

except ValueError:
    print("That is not a number.")