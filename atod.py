# File: atod.py
# Author: Mirko (xiang@bu.edu)
# Description: with an input of an angle, the program will yield the distance that the cannon ball will travel to
# Assignment: A04
# Date: 09/12/13

import math

def main():

    angle=input ("please enter an angle in degrees to aim the cannon:")

    radianceangle=math.radians(angle)

    distance= (40000/9.8)*math.sin(2*radianceangle)
    print
    print " You have aimed the cannon at",angle,"degrees"
    print
    print " You will hit a target",round(distance,2), "meters away"
    

main()
