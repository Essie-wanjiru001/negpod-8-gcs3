#!/usr/bin/python3
def print_int_only():
    num = input("please enter a number ")
    num = int(num)
    for i in range(0, num):
        if i % 2 != 0:
            print(i, end=", ")
    if num % 2 != 0:
        print(num)
