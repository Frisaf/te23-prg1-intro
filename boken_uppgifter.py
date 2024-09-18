import random

# UPPGIFT 3.6

# age = int(input("How old are you?\n> "))

# if age > 100:
#     print("Old")

# else:
#     print(f"Okay, so you will be {age + 1} next year :D")

# UPPGIFT 3.1
# print("Det finns tre olika abonemang: Kontant, Normal och Plus.\nKontant: Billigast om du ringer högst 33 minuter per månad.\nNormal: Bäst om du ringer mellan 33 och 66 minuter per månad.\nPlus: Om du ringer mer än så är detta mest förmånligt.")

# while True:
#     try:
#         call_len_aprox = int(input("Hur länge tror du att du kommer att samtala per månad?\n> "))

#         if call_len_aprox < 33:
#             print("Du borde skaffa kontant.")
    
#     except ValueError:
#         print("Det är inte en siffra.")

# UPPGIFT 4.6
# term = 1

# while True:
#     summa = 1/term
#     print(summa)
#     term += 1

#     if summa < 0.00001:
#         print(summa)
#         break

#     else:
#         continue

# UPPGIFT 4.7

judges= ["judge_1", "judge_2", "judge_3", "judge_4", "judge_5"]

if len(judges) >= 3:
    print("3 judges are present")

else:
    print("We need more judges.")

running = "running"

while running == "running":
    judge_scoring = [random.randint(0, 10) for _ in range(5)]

    print(f"The judges have judged: {', '.join(map(str, judge_scoring))}")
    
    true_sum = sum(judge_scoring) - min(judge_scoring) - max(judge_scoring)
    true_score = true_sum/3

    print(true_score)