#File: caesarcipher02.py
#Author: Mirko(xiang@bu.edu)
#Description:
#Assignment: A07
#Date: 09/24/13

def main():


      string = raw_input("Please enter your encripted phrase:")
      x=input("Please enter the key with a + o - symbol:")
      phrase=string.upper()
      phrase=phrase.split()
      sol=""
      
      
 
      for word in phrase:
            decoded=""
            for ch in word:
                  num= (((ord(ch)-65)+x)%26)+65
                  decoded=decoded+chr(num)
            sol=sol+decoded+" "
     
      print "your decoded phrase is:",sol
          
       
main()
        
