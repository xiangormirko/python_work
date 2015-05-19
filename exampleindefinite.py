#File: Exampleindefinite.py
#Author: Mirko (xiang@bu.edu)

def main():
    
    total=0
    i=0
    items=input("How many observations?")

    while i < items:

        value=input ("Enter the value for the next obersations %d:" %i)

        total+= value

        i+=1

    average= total/float(items)

    print "the total is %.2f" %total
    print "the average is %2.f" % average

main()
