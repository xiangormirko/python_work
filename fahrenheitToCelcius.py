# File: fahrenheitToCelcius.py
# Author: Mirko (xiang@bu.edu)
# Despription: Converts Fahrenheit to Celcius
# Assignment: A02
# Date: 09/05/13

def main() :

    # Collect an input
    fahrenheit= input ("Enter the temperature in Fahrenheit:")



    # spprocess the algorithm
    # C= (F- 32)/1.8
    # F= C*1.8+32
    celcius= (fahrenheit-32)/1.8

    # provide output to user
    print fahrenheit, "fahrenheit degrees is equivalent to", celcius,"celcius degrees"

main()
