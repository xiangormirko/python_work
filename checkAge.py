# File:checkAge.py
# Author: Mirko (xiang@bu.edu)
# Description: checks for age
# Assignment: A11
# Date: 10/08/13

def main():

    age= input("What is your age?:")

    while age<21:
        print "Bzzt! You are not old enough to drink."
        print
        age=input("What is your age?:")
        
    print "Okay! You are old enough to drink."

main()
               
