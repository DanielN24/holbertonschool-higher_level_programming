#!/usr/bin/python3
""" Write to a file """


def write_file(filename="", text=""):
    """ function that writes a string to a text file
    and returns the number of characters written """
    with open("my_first_file.txt", mode="w", encoding="UTF8") as myFile:
        myFile.write("This School is so cool!\n")
        return(myFile.write(text))
