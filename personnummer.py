#! /usr/bin/python3
import sys

for line in sys.stdin:
    data = line

    birth_year = str(data)[0:2]
    plus_minus = str(data)[6]

    if 40 <= int(birth_year) <= 99 and plus_minus == "+":
        result = "18" + birth_year + str(data)[2:6] + str(data)[7:]
    
    elif 00 <= int(birth_year) <= 19 and plus_minus == "+":
        result = "19" + birth_year + str(data)[2:6] + str(data)[7:]
    
    elif 20 <= int(birth_year) <= 99:
        result = "19" + birth_year + str(data)[2:6] + str(data)[7:]
    
    elif 00 <= int(birth_year) <= 19:
        result = "20" + birth_year + str(data)[2:6] + str(data)[7:]
    
    print(result)