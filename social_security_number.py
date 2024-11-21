#! /usr/bin/python3
import sys
import random

for line in sys.stdin:
    data = line

    while True:
        try:
            birth_year = int(input("Which year were you born?\n> "))
            break

        except ValueError:
            print("Please provide a valid year.")

    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,
    }

    while True:
        birth_month = input("Which month were you born?\n> ").title()
        
        if birth_month in months.keys():
            if months[birth_month] < 10:
                month_number = "0" + str(months[birth_month])
                break

            else:
                month_number = str(months[birth_month])
                break
        
        else:
            print("Please provide a valid month.")

    while True:
        try:
            birth_date = int(input("Which date were you born?\n> "))
            
            if 0 < birth_date <= 31:
                break

            else:
                print("Please provide a valid date.")

        except ValueError:
            print("Please provide a valid date.")

    social_security = str(birth_year) + str(month_number) + f"{birth_date:02d}"
    secret_digits = "".join(map(str, random.sample(range(1, 9), 4)))

    print(f"Your social security number: {social_security}-{secret_digits}")