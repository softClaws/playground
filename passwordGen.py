#!/usr/bin/python3
import random
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1 = chr(random.randint(65, 90))
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter2 = chr(random.randint(97, 112))
lowercaseLetter1 = chr(random.randint(97, 112))
numeric = chr(random.randint(48, 57))
password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1+ lowercaseLetter2 + numeric + numeric
password = shuffle(password)
print(password)