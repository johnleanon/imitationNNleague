import win32api as wapi
import time

keyList = ["\b"]
for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 123456789,.'APS$/\\":
    keyList.append(char)


def key_check():
    keys = []
    for key in keyList:
        if wapi.GetAsyncKeyState(ord(key)):
            keys.append(key)
    if 'H' in keys:
        return 'H'
    elif 'B' in keys:
        return 'B'
    elif 'A' in keys:
        return 'A'
    elif 'D' in keys:
        return 'D'
    elif ' ' in keys:
        return ' '
    elif 'Q' in keys:
        return 'Q'
    elif 'W' in keys:
        return 'W'
    elif 'E' in keys:
        return 'E'
    elif 'R' in keys:
        return 'R'
    elif 'F' in keys:
        return 'F'
    elif 'P' in keys:
        return 'P'
