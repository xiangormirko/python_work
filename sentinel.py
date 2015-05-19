#File: sentinel.py
#Author: Mirko (xiang@bu.edu)

def main():
    
    total=0
    i=0
    value= input("Enter the value for the next observation:")

    while value != -1:

        total+=value

        i+=1
        value=input ("Enter the value for the next obersations, or -1 to quit:")

 

    average= total/float(i)

    print "the total is %.2f" %total
    print "the average is %2.f" % average

main()
