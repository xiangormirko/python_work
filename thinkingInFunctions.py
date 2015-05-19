# File: thinkingInFunctions.py
# Author: Mirko (xiang@bu.edu)
# Description:
# Assingment: A09
# Date: 10/01/13

def dollarFormat(amount):

    dollar= "$ "+"%4.2f" %amount
    return dollar



def calculateBMI(height,weight):

    kilos= weight*0.4536
    meters= height*0.0245

    bmi= (kilos/ (meters*meters))

    return bmi

def main():

    amount=input("Please enter a dollar amount:")

    print "Your amount is:", dollarFormat(amount)

    height=input("Please enter your height in inches:")
    weight=input("Please enter your weight in pounds:")

    print "Your BMI is:", round(calculateBMI(height,weight),2)

main()
