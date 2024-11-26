#! /usr/bin/python3
import sys

for line in sys.stdin:
    data = int(line)

    one = "1"

    digits = len(str(data))
    bills = 0
    
    while True:
        number = digits * one
        division = int(data/int(number))
        data -= division * int(number)
        digits -= 1
        bills += division

        if not data % int(number) != 0:
            break

    print(bills)