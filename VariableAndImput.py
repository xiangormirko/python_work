# file: variableAndInput.py
# Author: Mirko (xiang@bu.edu)
# Description: demonstrate use of variables to hold onto data within a program.

# variable: a storage location within the computer's memory
# identifier: a name chosen to refer to the variable.
# - must not be keyword
# - must begin with a letter
# - no spaces
# expression:something that generates a value

# define a main function

def main():

    # assignment statemen: give a value to a variable
    # <var>= <expression>
    number= input("what is your favorite number:")
    print "your entered:", number

    # collect text input using: raw_input ( )

    name= raw_input("enter your name:")
    print "hello", name

# tell the program to execute the main function
main()
