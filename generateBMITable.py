# File: generateBMITable.py
# Author: Mirko (xiang@bu.edu)
# Description:
# Assingment: A09
# Date: 10/01/13

def calculateBMI(height,weight):

    kilos= weight*0.4536
    meters= height*0.0254

    bmi= (kilos/ (meters*meters))

    return bmi

def printBMITable(starth,endh,startw,endw):

    print "HEIGHT   WEIGHT--->"
    print "  ",
    for numbers in range (startw,endw+1,10):
        print "%6d" %numbers,
    print
    print
    
    for numb in range(starth,endh+1):
        
        print numb,
        for num in range(startw,endw+1,10):
            print "%6.2f" %round(calculateBMI(numb,num),1),
        print 
        
        
        
   

def main():

    begh=input("Please enter your beginning height:")
    endh=input("Please enter your ending height:")
    begw=input("Please enter your beginning weight:")
    endw=input("Please enter your ending weight:")

    printBMITable(begh,endh,begw,endw)

main()
