#!/usr/bin/env python3

import argparse
import string
import sys
#
# Set up CLI argument parsing.
#
parser = argparse.ArgumentParser()
parser.add_argument('--asciitorot', help='Convert plain text to ROT13 cipher.', action='store_true')
parser.add_argument('--rottoascii', help='Convert ROT13 to plain text.', action='store_true')
args = parser.parse_args()

#ROT13 intab and outtab representing the conversion
intab = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
outtab = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"

try:
    if args.asciitorot:
        str = args.asciitorot
        trantab = str.maketrans(intab,outtab)
        print(str.translate(trantab))
    elif args.rottoascii:
        str = input("[ROT13 --> ASCII selected]--String:> ")
        trantab = str.maketrans(outtab,intab)
        print(str.translate(trantab))
    else:
        sys.exit()
except KeyboardInterrupt:
    print("User exited voluntarily")