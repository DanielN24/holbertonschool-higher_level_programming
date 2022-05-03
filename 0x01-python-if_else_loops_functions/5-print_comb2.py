#!/usr/bin/python3
for zero_to_nine in range(00, 100):
    if zero_to_nine < 99:
        print("{0:02d}".format(zero_to_nine), ',', end='')
    else:
        print(zero_to_nine)
