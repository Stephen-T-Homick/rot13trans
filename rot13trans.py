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
    if not len(sys.argv) > 1:
        print("No arguments entered.")
        sys.exit()
    if args.asciitorot:
        strput = input("[ASCII --> ROT 13 Selected]--String:> ")
        trantab = strput.maketrans(intab,outtab)
        print(strput.translate(trantab))
    elif args.rottoascii:
        strput = input("[ROT13 --> ASCII selected]--String:> ")
        trantab = strput.maketrans(outtab,intab)
        print(strput.translate(trantab))
    else:
        sys.exit()
except KeyboardInterrupt as e:
    print("Exiting.")