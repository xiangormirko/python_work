#!/usr/bin/python

# File: quoteOfTheDay.py
# Author: Mirko (xiang@bu.edu)
# Assingment A17


import time 
import random

if __name__== "__main__":

    print "Content-type: text/html"
    print
    
    number= random.randint(0,5)
    einstein=["Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning",
              "The difference between stupidity and genius is that genius has its limits",
              "A person who never made a mistake never tried anything new",
              "Try not to become a man of success, but rather try to become a man of value",
              "In the middle of difficulty lies opportunity",
              "If you can't explain it simply, you don't understand it well enought"]

    pictures=["einstein1.jpg","einstein2.jpg","einstein3.jpg","einstein4.jpg","einstein5.jpg","einstein6.jpg"]

    quote=einstein[number] 
    pic=pictures[number]
    print """
<html>
<head>
<title> Quotes of the day!</title>
</head>

<body>

<center><font size="25" color="green">Albert Einstein's pearls of wisdom</font></center>
</p>
<center>brought to you by Xiang Zhao Mirko</center>
</p>

<center><table border=2></center>
    <tr>
    <td><font size="25" color="blue"> %s </font></td>
</p>
<center><table border=2></center>
    <tr>
    <td><img src= %s width=400 height=300</td>

</p>
This page was generated at: %s



</body>
</html>

""" % (quote,pic,time.ctime())

