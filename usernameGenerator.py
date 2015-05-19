# File= usernameGenerator.py
# Author= Mirko (xiang@bu.edu)
# Description= the program gathers input, greets, and generates a username
# Assignment= A06
# Date= 09/19/13

def main():

    lastname=raw_input("Enter your last name:")
    firstname=raw_input("Enter your first name:")
    middlename=raw_input("Enter your middle name:")
    name= firstname+" "+lastname+"."
    username=firstname[0]+middlename[0]+lastname[0:6]
    print
    print "welcome, %s" %name
    print
    print "Your username is %s." %username


main()
