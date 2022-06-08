#!/usr/bin/python3
""" reads a text file """


def read_file(filename="my_file_0.txt"):
    """ function that reads a text file and prints it to stdout """
    with open("my_file_0.txt", mode="r", encoding="UTF8") as myFile:
        print(myFile.read())
