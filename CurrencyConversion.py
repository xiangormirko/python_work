# File: currencyConversion.py
# Author: Mirko (xiang@bu.edu)
#Description: Demonstrate the input-process-output design pattern.

# design pattern: a re-usable model for creating a program/
# input-process-output pattern: the most basic model for a program which takes
# one or several inputs from the user, applies a "computation process, and provides
# an output back to the user.

def main() :

    # collect an input
    pesos= input ("Enter the price in pesos:")
    
    

    # process the algorithm
    # 1 peso == 0.075 dollars
    dollars= pesos * 0.075

    # provide output to user
    print pesos, "pesos is equivalent to", dollars, "dollars"


main() 
