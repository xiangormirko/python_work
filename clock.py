# File: clock.py
# Author: Mirko (xiang@bu.edu)
# Description: Definite Loop Exercise
# Assignment: A03
# Date: 09/10/13

def main():

    print "enter time in 24h format"
    StartHour=input("enter the start hour:")
    EndHour=input("enter the end hour:")
    IncrementMinutes=input("enter the increment in minutes:")

    for hour in range (StartHour,EndHour,1):
            for minutes in range (0,60,IncrementMinutes):
                print hour, ":", minutes
   
    print "time is up!"
            
               
            




main()
