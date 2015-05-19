# File: timeInMeters.py
# Author: Mirko (xiang@bu.edu)
# Description: converts the current time into distance in meters

# Assignment: A02
# Date: 09/05/13


def main():

    # collect 3 inputs
    print "please provide the exact time"
    hours= input("hour:")
    minutes= input ("minutes:")
    seconds= input ("seconds:")



    # process algorythm
    # meters= [(hours*60*60)+(minutes*60)+seconds]*299792458
    meters= ((hours*60*60)+(minutes*60)+(seconds))*299792458



    # provide output
    print meters, "meters is the time you are looking for"





main()
