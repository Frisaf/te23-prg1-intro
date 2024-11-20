apple_price = 7 # kr
pear_price = 13 # kr

while True:
    try:
        axel_apples = int(input("How many apples did Axel sell?\n> "))
        petra_pears = int(input("How many pears did Petra sell?\n> "))
        break
    
    except ValueError:
        print("Please type a number.")

axel_income = axel_apples * apple_price
petra_income = petra_pears * pear_price

if axel_income > petra_income:
    print(f"Axel sold {axel_apples} apples and earned {axel_income} kr. He earned more money than Petra, who earned {petra_income} kr and sold {petra_pears} pears.")

elif axel_income < petra_income:
    print(f"Petra sold {petra_pears} pears and earned {petra_income} kr. She earned more money than Axel, who earned {axel_income} kr and sold {axel_apples} apples.")

else:
    print(f"They earned the same amount of money, e.g {axel_income}. Axel sold {axel_apples} apples and Petra sold {petra_pears} pears.")