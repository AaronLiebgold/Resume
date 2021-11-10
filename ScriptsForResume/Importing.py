#!/usr/bin/env python3 

# Importing functions from another file/Script

from C2F import Celsius
from F2C import fahrenheit

#asking the user which conversion they would like to make

inputMeasure = input ("Would you like to Convert Tempeture to Fahrenheit or to Celsius?: ")

#calling the function to execute which inturn will ask the user what tempeture they want to convert

if inputMeasure != "Fahrenheit":
    print(fahrenheit())

if inputMeasure == "Fahrenheit":
    print(Celsius())
