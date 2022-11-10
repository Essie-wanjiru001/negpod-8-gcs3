#!/usr/bin/python3
def no_last_char():
    string = input("please enter characters ")
    x = len(string)
    for i in range(x - 2):
        print(string[i], end=", ")
    print(string[-2])
