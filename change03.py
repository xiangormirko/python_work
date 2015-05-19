#File: change.py
#Author: Mirko (xiang@bu.edu)
#Description: with an amount less than 100 cents, the program gives back the amount to minimize change in coins
#Assignment: A04
#Date: 09/12/13


import math

def main():

    price=input ("enter a price in cents less than 100:")

    print "here is the change that uses the fewest coins"

    change=100-price

    dimes= (change%25)/10
    print dimes

    quaters= change/25
    print quaters
    

main()
