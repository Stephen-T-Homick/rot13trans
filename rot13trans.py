#!/usr/bin/env python3

import argparse
import random
import string
import sys
# This script will accept input which will turn ASCII -> ROT13 or vice versa.
# Command strings are accepted internally as to not pollute .bash_history with private text.
# Usage ./rot13trans.py -h
###
###

# Set up CLI argument parsing.
###
parser = argparse.ArgumentParser()
parser.add_argument(
    '--asciitorot', help='Convert plain text to ROT13 cipher.', action='store_true')
parser.add_argument(
    '--rottoascii', help='Convert ROT13 to plain text.', action='store_true')
parser.add_argument(
    '--rot', help='Which ROT translation you would like to use', type=int)
args = parser.parse_args()

# Dict experimenting with both in / out tab's based on their ROT's.
# intab14 = "ABCDEFGHIJKLMNabcdefghijklmnOPQRSTUVWXYZABnopqrstuvwxyza"
# outtab14 = "NOPQRSTUVWXYZAnopqrstuvwxyzaABCDEFGHIJKLMNabcdefghijklmn"

# ROT13 intab and outtab representing the conversion
# intab13 = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
# outtab13 = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"


def usage():
    print("""
    usage: rot13trans.py [-h] [--asciitorot] [--rottoascii] [--rot 13]

Optional arguments:
  -h, --help    show this help message and exit

Required arguments:
--rot
[Without this argument, there will be no substitution cipher in place, and the script will exit.]
  
  """)


n = args.rot
# if args.rot:
#     print("You entered %d") % (args.rot)
while True:
    try:
        if not len(sys.argv) > 1:
            print("No arguments entered.")
            usage()
            sys.exit()
        if not args.rot:
            usage()
            sys.exit()
        if args.asciitorot:
            strput = input("[ASCII --> ROT 13 Selected]--String:> ")
            # trantab = strput.maketrans(intab,outtab)
            # print(strput.translate(trantab))
            output = []
            for c in strput:
                i = ord(c)
                i = int(i) + n
                # TODO: this can probably be simplified (DRY)
                if i > 65 and i <= (90 + n):
                    if i > 90:
                        i = i - 26
                if i > 97 and i <= (122 + n):
                    if i > 122:
                        i = i - 26
                o = (chr(i))
                output.append(o)
            output = ''.join(output)
            # TODO: Figure out the math to make sure the add/subtract doesn't go outside the ascii codes for a-z and A-Z (97-122 and 65-90)
            print(output)
        elif args.rottoascii:
            strput = input("[ROT13 --> ASCII selected]--String:> ")
            trantab = strput.maketrans(outtab, intab)
            print(strput.translate(trantab))
        else:
            print("Something else went wrong. Exiting.")
            usage()
            sys.exit()
    except KeyboardInterrupt as e:
        print("Exiting.")
        sys.exit()
