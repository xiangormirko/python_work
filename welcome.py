#!/usr/bin/python
# File: welcome.py
# Author: Mirko (xiang@bu.edu)

import time
import cgi
import cgitb; cgitb.enable()

print "Content-Type: text/html"
print


####################################################################
def doHTMLHead(title):

    print"""
<html>
<head>
<title>%s</title>
</head?
<body>
""" % title

####################################################################

def doHTMLTail():
    print"""
<hr>
This page was generated at%s/
</html>
""" % time.ctime()

####################################################################

def showInputForm():
    print"""
    <h2> Who Goes There?</h2>
    <form>
        <label>Name:</label>
        <input type="text" name="yourname">
        <input type="submit" name="submit" value="Let me in">
    </form>
    """


####################################################################

def showWelcomePage(yourname):

    print"""
    Welcome back, %s!
    <p>
    We're so glad you came to visi today
    <p>
    <a href="http://cs-webapps.bu.edu/cs108/xiang/welcome.py">
    Return to first page</a>.

    """ % yourname

    
####################################################################

if __name__ == "__main__":


    form= cgi.FieldStorage()

    doHTMLHead("Who's there?")

    if "yourname" in form:
        yourname= form["yourname"].value
        showWelcomePage(yourname)
        
    else:
        
        showInputForm()

    doHTMLTail()
    
