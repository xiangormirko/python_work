# File:guessing.py
# Author: Mirko (xiang@bu.edu)
# Description: guessing game
# Assignment: A11
# Date: 10/08/13

import random

def main():
    secret= random.randint(1,10)
    guess=input("guess a number between 1 and 10:")

    while guess !=secret:
        if guess>10:
            print "Invalid guess"
        if guess<1:
            print "Invalid guess"
        if guess>secret:
            print "too hight"
        if guess<secret:
            print "too low"
        guess=input ("guess again:")
    print "You got it!"
    

main()
