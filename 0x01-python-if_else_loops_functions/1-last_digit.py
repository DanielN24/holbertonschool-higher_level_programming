#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = num
if number >= 0:
    ln = num % 10
    if ln > 5:
        print("Last digit of", num, "is", ln, "and is greater than 5")
    elif ln < 6 and ln != 0:
        print("Last digit of", num, "is", ln, "and is less than 6 and not 0")
    else:
        print("Last digit of", num, "is", ln, "and is 0")

if num < 0:
    ln = num % -10
    if ln > 5:
        print("Last digit of", num, "is", ln, "and is greater than 5")
    elif ln < 6 and ln != 0:
     print("Last digit of", num, "is", ln, "and is less than 6 and not 0")
    else:
        print("Last digit of", num, "is", ln, "and is 0")
