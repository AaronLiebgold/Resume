#!/usr/bin/env python3

import argparse 


# instantiate ArgumentParser and bind it to a variable 
# the description string is used in the generated help text

parser = argparse.ArgumentParser(description='This script is used to generate a receipt for a transaction.')

# use add_argument function to add a set of available arguments
# note that we are assigning new names using the 'dest' keyboard
# dest is used to create a new property name for our object (argsFromCommandLine) below
# dest does not create a new object that we can reference in the script

parser.add_argument('-f', '--fruit', type=str, dest='fruitname', required=True, default=None, help='The name of the fruit we are selling.')
parser.add_argument('-p', '--price', type=float, dest='priceOfFruit', required=True, default=None, help='The price of your fruit.')
parser.add_argument('-t', '--tax', type=float, dest='taxRate', required=True, default=None, help='The tax rate for this transaction.')
parser.add_argument('-q', '--quantity', type=int, dest='numberOfFruit', required=True, default=None, help='The number of items to price.')
parser.add_argument('-b', '--border', type=str, dest='receiptBorder', required=True, default=None, help='The character to use when drawing the receipt border.')

# use parse_args funtion to process and validate the arguments being passed
# note that out variables from the comand line are properties on this named object (argsFromCommandLine)

argsFromCommandLine = parser.parse_args()

# Perform some calculations using input from command line

costOfFruit	= argsFromCommandLine.priceOfFruit * argsFromCommandLine.numberOfFruit
totalTax	= costOfFruit * argsFromCommandLine.taxRate
totalCostAndTax	= costOfFruit + totalTax

# print the receipt

def print_receipt():
    print('Welcome to the receipt Generator')
    print('\nHere is your receipt')
    print(argsFromCommandLine.receiptBorder * 40)
    print('Item\t\tQuantity\tPrice')
    print(argsFromCommandLine.receiptBorder *40)
    print(f'{argsFromCommandLine.fruitname}\t\t{argsFromCommandLine.numberOfFruit}\t\t${argsFromCommandLine.priceOfFruit:.2f}')
    print(argsFromCommandLine.receiptBorder * 40)
    print(f'Total Cost\t\t\t${costOfFruit:.2f}')
    print(f'Total Tax\t\t\t${totalTax:.2f}')
    print(f'Amount Due\t\t\t${totalCostAndTax:.2f}')
    print(argsFromCommandLine.receiptBorder * 40)

if __name__ == '__main__':
    print_receipt()
