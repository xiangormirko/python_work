#File: caesarcipher01.py
#Author: Mirko(xiang@bu.edu)
#Description:
#Assignment: A07
#Date: 09/24/13

def main():


      string = raw_input("Please enter your encripted word:")
      x=input("Enter the key with a + or - sign:")
      phrase=string.upper()
      sol=""
      
 
      for ch in phrase:
          num= (((ord(ch)-65)+x)%26)+65
          sol=sol+chr(num)
      print
      print "your decoded word is:",sol
          
       
main()
        
