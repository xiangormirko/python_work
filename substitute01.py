# File: substitute01.py
# Author: Mirko (xiang@bu.edu)
# Description:collect an input and substitues a word for another word
# Assignment: A07
# Date: 09/24/13

def main():

    phrase= raw_input("Enter a phrase:")
    substring= raw_input("Enter a word in this phrase to replace:")
    replacement= raw_input("Enter a word to be the replacement:")

    print phrase.replace(substring,replacement)


main()
