# File: savings01.py
# Author: Mirko (xiang@bu.edu)
# Description:accumulating monthly interest
# Assignment: A05
# Date: 09/17/13


def main():
    goal= input("Enter your savings goal in dollars:")
    YearRatepercent= input("Enter the expected annual rate of return in percent:")
    yearRate=YearRatepercent/100
    Time=input("Enter time until goal in year:")
    MonthRate= yearRate/12
    nominatore=MonthRate*goal
    denominatore=((1+MonthRate)**(Time*12))-1
    MonthSavings= nominatore/denominatore
    interest=0
    balance=0

    print
    print "Saving goal: $", goal
    print "Annual rate of return:", yearRate,"(",YearRatepercent,"%)"
    print
    


    for i in range(1,Time+1,1):
        print "Saving Schedule for year",i
        pastinterest=interest
        for num in range (1,13,1):
            
            interestearned= balance*MonthRate
            interest=interest+interestearned
            balance=balance+MonthSavings+interestearned
            
            print "month    interest   amount    balance"
            print  num,"      ",round(interestearned,2),"20   ",round(MonthSavings,2),"   ",round(balance,2)
        print
        print "Savings summary for year", i
        print "Total amount saved:", round(MonthSavings*12,2)
        print "Total interest earned:", round(interest-pastinterest,2)
        print "End of your balance:", round(balance,2)
        print
        print "***************************************************************************"
        print

main()
        
