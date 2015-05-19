#File: average03.py
#Author: Mirko (xiang@bu.edu)

def main():
    
    total=0
    i=0
    response= "yes"

    while response =="yes":

        value=input ("Enter the value for the next obersations %d:" %i)

        total+= value

        i+=1

        response= raw_input( "Do you have more inputs? (yes/no):")

    average= total/float(i)
    print "the total is %.2f" %total
    print "the average is %2.f" % average
main()
