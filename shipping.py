#!/usr/bin/python

# File: shipping.py
# Author: Mirko (xiang@bu.edu)
# Assignment: A18

import cgi
import cgitb; cgitb.enable()
import time
import smtplib

print "Content-type: text/html"


##########################################################################
def printShippingForm():
	print """
<body>

<hr>

<h2> A Contact Form </h2>
<form action="http://cs-webapps.bu.edu/cs108/xiang/shipping.py">
<table border=1>
<tr>
<td><label>Name:</label><input type="text" name="name"><br></td>
<tr>
<td><label>Address:</label>
<input type="text" name="address"><br></td>
<tr>
<td><label>State:</label>
<select name="state" size="1">
  <option value="AL">Alabama</option>
  <option value="AK">Alaska</option>
  <option value="AZ">Arizona</option>
  <option value="AR">Arkansas</option>
  <option value="CA">California</option>
  <option value="CO">Colorado</option>
  <option value="CT">Connecticut</option>
  <option value="DE">Delaware</option>
  <option value="DC">Dist of Columbia</option>
  <option value="FL">Florida</option>
  <option value="GA">Georgia</option>
  <option value="HI">Hawaii</option>
  <option value="ID">Idaho</option>
  <option value="IL">Illinois</option>
  <option value="IN">Indiana</option>
  <option value="IA">Iowa</option>
  <option value="KS">Kansas</option>
  <option value="KY">Kentucky</option>
  <option value="LA">Louisiana</option>
  <option value="ME">Maine</option>
  <option value="MD">Maryland</option>
  <option value="MA">Massachusetts</option>
  <option value="MI">Michigan</option>
  <option value="MN">Minnesota</option>
  <option value="MS">Mississippi</option>
  <option value="MO">Missouri</option>
  <option value="MT">Montana</option>
  <option value="NE">Nebraska</option>
  <option value="NV">Nevada</option>
  <option value="NH">New Hampshire</option>
  <option value="NJ">New Jersey</option>
  <option value="NM">New Mexico</option>
  <option value="NY">New York</option>
  <option value="NC">North Carolina</option>
  <option value="ND">North Dakota</option>
  <option value="OH">Ohio</option>
  <option value="OK">Oklahoma</option>
  <option value="OR">Oregon</option>
  <option value="PA">Pennsylvania</option>
  <option value="RI">Rhode Island</option>
  <option value="SC">South Carolina</option>
  <option value="SD">South Dakota</option>
  <option value="TN">Tennessee</option>
  <option value="TX">Texas</option>
  <option value="UT">Utah</option>
  <option value="VT">Vermont</option>
  <option value="VA">Virginia</option>
  <option value="WA">Washington</option>
  <option value="WV">West Virginia</option>
  <option value="WI">Wisconsin</option>
  <option value="WY">Wyoming</option>
</select><br></td>
<tr>
<td><label>Zip code</label>
<input type="text" name="zipcode"><br></td>
<tr>
<td><label>Total purchase amount:</label>
<input type="text" name="totamount"><br></td>
<tr>
<td>Optional additions:<br>
<input type="checkbox" name="optional" value="Card"><label>Card Message $1</label><br>
<input type="text" name="optional" ><br>
<input type="checkbox" name="optional" value="Wrap"><label>Giftwrap</label><br>
<br></td>
<tr>
<td>Shipping method:<br>
<input type="radio" name="shipping" value="6week"><label>6-Week $0.00</label><br>
<input type="radio" name="shipping" value="standard"><label>Standard $4.99</label><br>
<input type="radio" name="shipping" value="2day"><label>2nd Day $9.99</label><br>
<input type="radio" name="shipping" value="overnight"><label>Overnight $14.99</label><br></td>


<input type="hidden" name="mailto" value="xiangormirko@gmail.com">
<br>
<tr>
<td><input type="submit" value="Place Order"></td>
</form>

""" 
################################################################################
def doHTMLHead(title):

    print """
    <html>
    <body>
    <h1>%s</h1>

    <p>
    """ % title

################################################################################
def doHTMLTail():

    print """
    <p>
    This page was generated at %s.
    </body>
    </html>

    """ % time.ctime()

################################################################################

def printConfirmationPage(name,address,state,zipcode,totamount,shipping,optional):

    tot=float(totamount)
    
    if shipping =="overnight":
        tot=tot+14.99
        
    elif shipping=="standard":
        tot=tot+4.99
        
    elif shipping=="2day":
        tot=tot+9.99
        
    else:
        tot=tot

    if "Card" in optional:
        tot=tot+1

    if "Wrap" in optional:
        tot=tot+2


    

    print """
    <h1>Order Confirmed</h1>
    <p>
    <table border=1>
    <tr>
    <td>Name: %s</td>
    <tr>
    <td>Address: %s </td>
    <tr>
    <td><State: %s </td>
    <tr>
    <td>Zipcode: %s</td>
    <tr>
    <td>Shipping: %s</td>
    <tr>
    <td>Optional: %s</td>
    <tr>
    <td>Total Amount: %s</td>
    <tr>
    <td><a href="http://cs-webapps.bu.edu/cs108/xiang/shipping.py">
    Return to first page</a>.<br>
    </table>
    


    """ %(name,address,state,zipcode,shipping,optional,float(tot))


################################################################################

#def sendEmail(sender,recipient,msg):

#    smtp=smtplib.SMTP()

#    smtp.connect("acs-smtp.bu.edu",25)
#    r=smtp.helo("xiang")
#    print "smtp.helo returned",r
#    print "Connected to the SMTP server."

#    r=smtp.sendmail(sender,recipient,msg)

#    print "smtp.sendmail returned", r
#    print "Email was sent to %" % recipient

#    smtp.quit()
#    print "Disconnected from SMTP server."





################################################################################
if __name__== "__main__":

    form= cgi.FieldStorage()
	
    doHTMLHead("Custumer order information")
    
    if "name" in form and "address" in form and "state" in form and "zipcode" in form and "totamount" in form and "shipping" in form:

        
        name= form["name"].value
        address= form["address"].value
        state= form["state"].value
        zipcode=form["zipcode"].value
        totamount=form["totamount"].value
        totamount=float(totamount)
        shipping=form["shipping"].value
        optional=form.getlist("optional")
 
        printConfirmationPage(name,address,state,zipcode,totamount,shipping,optional)       


#        sender="xiangormirko@hotmail.com"
#        recipient="xiangormirko@gmail.com"
#        msg="ciao"
#        sendEmail(sender,recipient,msg)
        
    else:
        
    
        printShippingForm()
    
    doHTMLTail()
    
    
    
