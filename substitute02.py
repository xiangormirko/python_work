# File: substitute02.py
# Author: Mirko (xiang@bu.edu)
# Description:collects an input and replaces a word for a word
# Assignment: A07
# Date: 09/24/13

def main():

    phrase= raw_input("Enter a phrase:")
    substring= raw_input("Enter a word in this phrase to replace:")
    replacement= raw_input("Enter a word to be the replacement:")

    phrase.index(substring)
    
    len(substring)
    len(phrase)

    replaced= phrase[0:phrase.index(substring)]+replacement+phrase[phrase.index(substring)+len(substring):len(phrase)]
    print
    print replaced
main()
