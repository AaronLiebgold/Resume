#!/usr/bin/env python3

# This function will convert Celsius to Fahrenhheit

def Celsius():
    inputFahrenheit = input("Enter a tempeture you would like to convert to Fahrenheit: ")
    inputFahrenheitInteger = int(inputFahrenheit)
    Celsius = (inputFahrenheitInteger * 9/5) + 32
    print("The tempeture in Fahrenheit is")
    return(Celsius)

def main():
    print(Celsius())

if __name__ == "__main__":
    main()
