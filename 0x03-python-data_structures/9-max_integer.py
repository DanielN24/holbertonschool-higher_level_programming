#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest = -1
    for the_num in my_list:
        if the_num > biggest:
            biggest = the_num
    print(biggest)
