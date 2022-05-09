#!/usr/bin/python3
def element_at(my_list, idx):
    for numbers in range(len(my_list)):
        if idx < 0:
            return(NONE)
        if idx > len(my_list):
            return(NONE)
        return(my_list[idx])
