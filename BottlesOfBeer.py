# File: bottlesOfBeer.py
# Author: Mirko (xiang@bu.edu)
# Description: Definite Loop Exercise
# Assignment: A03
# Date: 09/10/13


def main():
    BeerBottles=input("What's the biggest number you can think of?")

    for BeerBottles in range (BeerBottles,2,-1):

        print BeerBottles,"bottles of beer on the wall,"
        print BeerBottles,"bottles of beer!"
        print "if one of those bottles should happen to fall..."
        print BeerBottles-1, "bottles of beer on the wall!"
        print

        
    print """2 bottles of beer on the wall,
2 bottles of beer!
if one of those bottles should happen to fall...
1 bottle of beer on the wall!"""
    print
    print """1 bottle of beer on the wall,
1 bottle of beer!
if one of those bottles should happen to fall...
0 bottles of beer on the wall!"""
    print
    print "congratulations! may your patience lead you to success in your life"

main()
