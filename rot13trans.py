#!/usr/bin/env python3

import argparse
import string
import sys
### This script will accept input which will turn ASCII -> ROT13 or vice versa.
### Command strings are accepted internally as to not pollute .bash_history with private text.
### Usage ./rot13trans.py -h
###
###

### Set up CLI argument parsing.
###
parser = argparse.ArgumentParser()
parser.add_argument('-a', '--asciitorot', help='Convert plain text to ROT13 cipher.', action='store_true')
parser.add_argument('-r', '--rottoascii', help='Convert ROT13 to plain text.', action='store_true')
parser.add_argument('-n', '--rotnumber', help='Convert ROT13 to plain text.', action='store_true', default='13', type=int)
args = parser.parse_args()

#ROT13 intab and outtab representing the conversion
intab = "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz"
outtab = "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm"
n = int(args.rotnumber)

def usage():
    print("""
    usage: rot13trans.py [-h] [-a, --asciitorot] [-r --rottoascii]

optional arguments:
  -h, --help    show this help message and exit
  -a, --asciitorot  Convert plain text to ROT13 cipher.
  -r, --rottoascii  Convert ROT13 to plain text.
  -n, --rotnumber  Pick a ROT number to translate too/from
  """)

while True:
    try:
        if not len(sys.argv) > 1:
            print("No arguments entered.")
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
                        i = i -26
                o = (chr(i))
                output.append(o)
            output = ''.join(output)
            # TODO: Figure out the math to make sure the add/subtract doesn't go outside the ascii codes for a-z and A-Z (97-122 and 65-90)
            print(output)
        elif args.rottoascii:
            strput = input("[ROT13 --> ASCII selected]--String:> ")
            trantab = strput.maketrans(outtab,intab)
            print(strput.translate(trantab))
        else:
            sys.exit()
    except KeyboardInterrupt as e:
        print("Exiting.")
        sys.exit()
