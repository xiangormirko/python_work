# File: savings01.py
# Author: Mirko (xiang@bu.edu)
# Description:accumulating monthly interest
# Assignment: A05
# Date: 09/17/13


def main():
    YearRate= 0.12
    MonthSavings= 500
    MonthRate= YearRate/12
    interest=0
    balance=0
    


    for i in range(1,3,1):
        print "Saving Schedule for year",i
        pastinterest=interest
        for num in range (1,13,1):
            
            interestearned= balance*MonthRate
            interest=interest+interestearned
            balance=balance+MonthSavings+interestearned
            
            print "month    interest   amount    balance"
            print  num,  round(interestearned,2),  round(MonthSavings,2),  round(balance,2)
        print
        print "Savings summary for year", i
        print "Total amount saved:", round(MonthSavings*12,2)
        print "Total interest earned:", round(interest-pastinterest,2)
        print "End of your balance:", round(balance,2)
        print
        print "***************************************************************************"
        print

main()
        
