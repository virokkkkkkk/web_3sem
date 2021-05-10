import re

def checkChars(number):
    acceptable_chars = ['1','2','3','4','5','6','7','8','9','0',' ','(',')','-','.','+']
    for char in number:
        if (char not in acceptable_chars):
            return False
    return True

def checkLength(number):
    # if (len(number) == 11):
    #     if (number[0] == '8' or number[0] == '8'):
    #         return True
    if (len(number) == 10):
        return True
    # if (len(number) == 12):
    #     if (number[0:2] == "+7" or number[0] == '8'):
    #         return True
    #     else:
    #         return False
    # elif (len(number) == 11):
    #     if (number[0:2] != "+7" and number[0] != '8'):
    #         return True
    return False

def formatNumber(number):
    rmChars = '-().+ '
    for char in rmChars:
        number = number.replace(char, "")
    if (number[0] == '7' or number[0] == '8'):
        return number[1::]
    return number

def formatNumberOut(number):
    mask = list("8-***-***-**-**")
    c = 0
    for i in range(2, len(mask)):
        if mask[i] == '*':
            mask[i] = number[c]
            c = c+1
    return ''.join(mask)

        



        