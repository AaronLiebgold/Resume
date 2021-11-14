#!/usr/bin/env python3

import argparse
import sys

parser = argparse.ArgumentParser(description="This is Aaron's Personalized Menu")

#================== Add arguments=============================================

##### Most Basic Example
parser.add_argument('-m', dest='myVariable', help='This is some text that will help you out')

##### This is how we input an integer of ports
parser.add_argument('-i', '--integer', dest='varInteger', metavar='[an integer]', default=10, type=int, required=False, help='<required> Enter a Simple Integer')

##### This is how we input a float
parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=10.0, type=float, required=False, help='Enter a simple Float')

##### This is how we input a string
parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='hello', type=str, required=False, help='Enter a simple String')

##### This is just passing a list to the argument (space delimited set of strings)
parser.add_argument('-l', dest='varList', metavar='[strings]', default=[], nargs='+', required=False, help='Enter a list of strings (space delimited)')

##### This is how we work with Boolean values #####
##### - This is False by default, use ‘-t’ to set it to True
parser.add_argument('-t', '--set-true', dest='bool_t', default=False, action='store_true', required=False, help='Toggle from default False to True')

##### - This is True by default, use ‘-f’ to set it to False
parser.add_argument('-f', '--set-false', dest='bool_f', default=True, action='store_false', required=False, help='Toggle from default True to False')

##### This is how we show the script version ######
parser.add_argument('-v','--version', action='version', version='%(prog)s 1.0')


#================ Using the parser =========================================

args = parser.parse_args()

#print(parser.print_usage())


#print('====================')

##### This is used to check if no arguments were passed.
##### If not print the -h (usage instructions)
if len(sys.argv) == 1:
    print(parser.print_help())
    exit(0)

print("The value of your '-m' arg is: " + str(args.myVariable))
print("The value of your '-i' arg is: " + str(args.varInteger))
print("The value of your '-d' arg is: " + str(args.varFloat))
print("The value of your '-s' arg is: " + str(args.varString))
print("The value of your '-t' arg is: " + str(args.bool_t))
print("The value of your '-f' arg is: " + str(args.bool_f))

print("=== Here is the List ===")
print(args.varList)
for arg in args.varList:
    print(arg)

