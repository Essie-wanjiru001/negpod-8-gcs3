#!/usr/bin/python3
def no_vowel():
    var = input("please enter a string: ")
    x = len(var)
    n_s = ""
    p = -1
    while p < x - 1:
        p += 1
        if var[p] != 'i' and var[p] != 'a' and var[p] != 'u' and var[p] != 'o' and var[p] != 'e' and var[p] != 'y':
            n_s += var[p]
    m = len(n_s)
    n = -1
    while n < m - 2:
        n += 1
        print(n_s[n], end='')
    print(n_s)
