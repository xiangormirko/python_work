# File: atod.py
# Author: Mirko (xiang@bu.edu)
# Description: with an input distance, the program will yield the angle that the cannon needs to fire
# Assignment: A04
# Date: 09/12/13

import math

def main():

    distance= input("please insert the distance in meters you want to reach with your cannonball:")


    radianceangle= (0.5)*math.asin(( 9.8/40000)*distance)

    angle=math.degrees(radianceangle)

    print
    print "in order to reach",distance
    print
    print "meters away, you need to set your cannon at" ,round(angle,2),"degrees"

main()
