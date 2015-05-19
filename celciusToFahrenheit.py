# File: celsiusToFahrenheit.py
# Author: Mirko (xiang@bu.edu)
# Despription: Converts Celsius to Fahrenheit
# Assignment: A02
# Date: 09/05/13

def main() :

    # Collect an input
    celcius= input ("Enter the temperature in Celcius:")



    # spprocess the algorithm
    # C= (F- 32)/1.8
    # F= C*1.8+32
    fahrenheit= celcius * 1.8 + 32

    # provide output to user
    print celcius, "celcius degrees is equivalent to", fahrenheit,"fahrenheit degrees"


main()
