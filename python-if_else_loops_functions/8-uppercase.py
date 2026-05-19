#!/usr/bin/python3
def uppercase(str):
    upped = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upped += chr(ord(c) - 32)
        else:
            upped += c
    print("{}".format(upped))
