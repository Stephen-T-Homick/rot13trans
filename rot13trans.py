#!/usr/bin/env python3

import string

#ROT13 intab and outtab representing the conversion
intab = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
outtab = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"

str = input("String:> ")
trantab = str.maketrans(intab,outtab)
print(str.translate(trantab))
