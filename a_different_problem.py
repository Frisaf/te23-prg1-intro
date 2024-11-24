#! /usr/bin/python3
import sys

for line in sys.stdin:
    data = line

    numbers = data.split()
    first_number = int(numbers[0])
    second_number = int(numbers[1])

    result = abs(first_number - second_number)
    print(result)