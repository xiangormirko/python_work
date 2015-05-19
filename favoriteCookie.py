#!/usr/bin/python
#
# file: favoriteCookie.py
# description: demonstration of cookies
# Author: Mirko (xiang@bu.edu)
#

import cgi
import cgitb; cgitb.enable()
import time
import Cookie
import os



################################################################################
def doHTMLHead(title):

    print "Content-Type: text/html"
    print

    print """
    <html>
    <head>
    <title>%s</title>
    </head>
    <body>
    """ % title


################################################################################
def doHTMLTail():

    print """
    <p>
    <hr>
    This page was generated at %s.
    </body>
    </html>

    """ % time.ctime()
    
##############################################################################
def doWelcomeIdentForm():

    print """
    <h2>Welcome</h2>
    You must identify yourself to use this website. Please enter your:
    <p>
    <form method="post">
    <table>
      <tr>
        <td>
          <h3>Email Address:</h3>
        </td>
        <td>
          <input type="text" name="email" size="20"><br>
        </td>
      </tr>
      <tr>
        <td>
          <h3>Password:</h3>
        </td>
        <td>
        <input type="password" name="password" size="20"><br>
      </tr>
      <tr>
        <td>
          <h3>Favorite Cookie:</h3>
        </td>
        <td>
          <input type="text" name="fav" size="20"><br>
        </td>
      </tr>
      <tr>
        <td>
        <input type="submit" name="login_button" value="Authenticate">
        </td>
        <td>
        </td>
      </tr>
    </table>
    </form>
    """

    
##############################################################################
def doAuthentication(form):

    # get email, password:
    email = form["email"].value
    password = form["password"].value
    favoriteCookie=form["fav"].value


    # run a query against the database, check if valid username
 
    # create a cookie, and send it to the client
    cookie= Cookie.SimpleCookie()

    cookie["remember_me"]= email
    cookie["whatever"]= "blahblahblah"
    cookie["favoriteCookie"]=favoriteCookie

    print cookie # writes an HTTP header

    
    # this function will print the rest of the HTTP headers
    doHTMLHead("Remember Me")

    print """
    Authentication complete, %s. You have been identified by our servers.
    """ % email

##############################################################################
def printWelcomeScreen(email,favoriteCookie):

    print """
    Hi %s. Welcome back. Your favorite cookie is %s.    
    """ % (email,favoriteCookie)

    
##############################################################################
if __name__ == "__main__":

    # read a cookie from the HTTP request:
    cs= os.environ["HTTP_COOKIE"]
    # CREATE A COOKIE OBJECT FROM THIS STRING

    cookie=Cookie.SimpleCookie()
    cookie.load(cs)
    form = cgi.FieldStorage()

    if "remember_me" in cookie:

        email=cookie["remember_me"].value
        favoriteCookie=cookie["favoriteCookie"].value
        printWelcomeScreen(email,favoriteCookie)


    
    # get form fields


    ## did the HTTP request give us a cookie

 
    ## if no cookie, check for login in process:
    elif "login_button" in form:

        doAuthentication(form)


    ## else, show the default login
    else:
        doHTMLHead("Remeber Me")
        doWelcomeIdentForm()
        doHTMLTail()
            
