print("Welcome to Kasper! You will, together with the computer, count from 1 and when you come to a number that is dividable or contains 7 or 11 you clap (don't provide a number and leave the input blank).")

while True:
    start_number = 1

    while True:
        if start_number % 7 == 0 or start_number % 11 == 0 or "7" in str(start_number) or "11" in str(start_number):
            print("*Clap!*")
            start_number += 1
        
        else:
            print(start_number)
            start_number += 1

        user_input = input("> ")

        if start_number % 7 == 0 or start_number % 11 == 0 or "7" in str(start_number) or "11" in str(start_number) and user_input == "":
            start_number += 1

        elif start_number % 7 == 0 or start_number % 11 == 0 or "7" in str(start_number) or "11" in str(start_number) and len(user_input) > 0:
            print("Oh no! You should have left the input blank... restarting the loop.")
            break

        elif int(user_input) != start_number and start_number % 7 != 0 and start_number % 11 != 0 and "7" not in str(start_number) and "11" not in str(start_number):
            print("Oh no! That's the wrong number! Restarting the loop...")
            break

        elif int(user_input) != start_number and (start_number % 7 == 0 or start_number % 11 == 0 or "7" in str(start_number) or "11" in str(start_number)):
            print("Oh no! That's the wrong number! Restarting the loop...")
            break

        else:
            start_number += 1