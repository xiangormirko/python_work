# File:craps.py
# Author: Mirko (xiang@bu.edu)
# Description: craps game
# Assignment: A11
# Date: 10/08/13

import random

def roll():
    dice1= random.randint(1,6)
    dice2= random.randint(1,6)
    comeout=dice1+dice2
    return comeout

def playRound():

    begin=raw_input("Hit ENTER to roll the dice...")


    comeout=roll()
    print "The come-out phase:"
    print "you rolled a",comeout
    print
    if comeout in (7,11):
        print "Natural, you win"
        return True
    elif comeout in (2,3,12):
        print "Crapping-out, you lose"
        return False
    else:
        print "The point phase"
        begin=raw_input("Hit ENTER to roll the dice...")
        point=roll()
        print "You rolled a",point
        print
        while point != comeout or point !=7:
            if point==7:
                print "Seven-out! you lose"
                return False
                break
            elif point==comeout:
                print "Hit, you win"
                return True
                break
            else:
                reroll=raw_input("Hit ENTER to reroll the dice...")
                point=roll()
                print "You rolled a", point
                print

        
def main():
    chips=100
    bet= input("Enter bet (0 to quit):")
    while bet>=1:
        
        if bet in range(chips+1):
        
            
        
        
            if playRound():
                chips+=bet
            else:
                chips-=bet
        else:
            print "invalid bet"
        print"you have %i chips left" %chips
        bet= input("Enter bet (0 to quit):")

main()
