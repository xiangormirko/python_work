#!/usr/bin/python
#
# "she-bang" line is a directive to the web server: where to find python
#
# filename: miniFacebook.py
# description: A simple version of the classic


import MySQLdb as db
import time
import cgi
import cgitb; cgitb.enable()
import random

print "Content-Type: text/html"
print "" # blank line

################################################################################
def getConnectionAndCursor():
    """
    This function will connect to the database and return the
    Connection and Cursor objects.
    """ 
    # connect to the MYSQL database
    conn = db.connect(host="localhost",
                      user="xiang",
                      passwd="8900",
                      db="xiang")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
def doHTMLHead(title):

    print """
    <html>
    <head>
    <center><title>%s</title>
    </head>
    <body>
    <h1>%s</h1></center>
    """ % (title, title)


################################################################################
def doHTMLTail():

    # always show this link to go back to the main page
    print """
    <p>
    <hr>
    <a href="./miniFacebook.py">Return to main page.</a><br>
    This page was generated at %s.
    </body>
    </html>

    """ % time.ctime()

################################################################################
def debugFormData(form):
    """
    A helper function which will show us all of the form data that was
    sent to the server in the HTTP form.
    """
    
    print """
    <h2>DEBUGGING INFORMATION</h2>
    <p>
    Here are the HTTP form data:
    """
    print """
    <table border=1>
        <tr>
            <th>key name</th>
            <th>value</th>
        </tr>
    """
    
    # form behaves like a python dict
    keyNames = form.keys()
    # note that there is no .values() method -- this is not an actual dict

    ## use a for loop to iterate all keys/values
    for key in keyNames:

        ## discover: do we have a list or a single MiniFieldStorage element?
        if type(form[key]) == list:

            # print out a list of values
            values = form.getlist(key)
            print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, str(values))

        else:
            # print the MiniFieldStorage object's value
            value = form[key].value
            print """
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
            """ % (key, value)
        
    print """
    </table>
    <h3>End of HTTP form data</h3>
    <hr>
    """

## end: def debugFormData(form)
    
    
################################################################################
def getAllUsers():
    """
    Middleware function to get all users from the profiles table.
    Returns a list of tuples of (idnum, lastname, firstname).
    """

    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT id, lastname, firstname
    FROM profiles
    """

    # execute the query
    cursor.execute(sql)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getAllUsers():

################################################################################
def getOneProfile(idNum):
    """
    Middleware function to retrieve one profile record from the database.
    Returns a list containing one tuple.
    """
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM profiles
    WHERE id=%s
    """

    # execute the query
    parameters = (int(idNum), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data

## end: def getOneProfile(idNum):


################################################################################
def showAllUsers(data):
    """
    Presentation layer function to display a table containing all users' lastnames
    and first names.
    """

    ## create an HTML table for output:
    print """
    <h2>User List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>lastname</b></font></td>
        <td><font size=+1"><b>firstname</b></font></td>
      </tr>
    """
    
    for row in data:

        # each iteration of this loop creates on row of output:
        (idNum, lastname, firstName) = row

        print """
      <tr>
        <td><a href="?idNum=%s">%s</a></td>
        <td><a href="?idNum=%s">%s</a></td>
      </tr>
        """ % (idNum, lastname, idNum, firstName,)
        

    print """
    </table>
    """
    print "Found %d users.<br>" % len(data)

## end: def showAllUsers(data):
    

################################################################################
def showProfilePage(data):
    """
    Presentation layer function to display the profile page for one user.
    """

    ## show profile information
    (idNum, lastname, firstName, email, activities) = data[0]

    print """
    <h2>%s %s's Profile Page</h2>
    <p>
    <table border=1>
        <tr>
            <td>Email</td>
            <td>%s</td>

        </tr>
        <tr>
            <td>Activities</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>
            <form>
            <input type="submit" name="beginUpdate" value="update">
            <input type="hidden" name="idNum" value="%s">
            </form>
        </tr>
    </table>
    """ % (firstName, lastname, email, activities,idNum)
    print"""
    
    <h2> Post a new status message</h2>
    <p>
    <form method="post" action=miniFacebook.py>
    <input type="hidden" name="idNum" value="%s">
    <input type="text" name="message">
    <input type="submit" name="post" value="post it!">
    </form>

    """ % (data[0][0])
    status=getStatusMessagesForUsers(idNum)
    showStatusMessagesForUsers(status)
    
    print """
    <h2> Add a new friend</h2>
    <form>
    <input type="text" name="friendID">
    <input type="hidden" name="idNum" value="%s">
    <input type="submit" name="addfriend" value="add friend!">
    </form>
    """ % (data[0][0])
    

    data=getFriends(idNum)
    
    showFriends(idNum,data)

    data=getNewsFeed(idNum)

    showNewsFeed(data)       
## end: def showProfilePage(data):
    
################################################################################
def getStatusMessagesForUsers(idNum):
    
    # connect to database
    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM status
    WHERE id=%s
    """

    # execute the query
    parameters = (int(idNum), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()
    
    return data
################################################################################
def showStatusMessagesForUsers(status):
    ## show profile information
    print"""
    <h2>Status Page</h2>
    <p>
    """
    for row in status:
        
        (date,idNum,message) = row

        print """

        <table border=1>
            <tr>
                <td>Date</td>
                <td>%s</td>
            </tr>
            <tr>
                <td>message</td>
                <td>%s</td>
            </tr>
        </table>
        """ % (date,message)

################################################################################
def showAddProfileForm():
    print """
    <h2> Create a new profile </h2>
    <form>
    <table border=1>
        <tr>
            <td>lastname</td>
            <td><input type="text" name="lastname"></td>
        </tr>
        <tr>
            <td>firstname</td>
            <td><input type="text" name="firstname"></td>
        </tr>
        <tr>
            <td>email</td>
            <td><input type="text" name="email"></td>
        </tr>
        <tr>
            <td>activities</td>
            <td><input type="text" name="activities"></td>
        </tr>
        <tr>
            <td><input type="submit" name="insertprofile" value="create">
        </td>
            </td>
        </tr>
    </table>
    </form>
    """

################################################################################
def showUpdateProfileForm(data):

    record= data[0]
    idNum= record[0]
    lastname=record[1]
    firstname=record[2]
    fields=record+(idNum,lastname,firstname)


    
    print """
    <h2> Update profile </h2>
    <form>
    <table border=1>
        <tr>
            <td>idNum</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>lastname</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>firstname</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>email</td>
            <td><input type="text" name="email" value="%s"></td>
        </tr>
        <tr>
            <td>activities</td>
            <td><input type="text" name="activities" value="%s"></td>
        </tr>
        <tr>
            <td><input type="submit" name="updateprofile" value="Update"></td>
            <td><input type="submit" name="cancel" value="Cancel Update"></td>
        </td>
            </td>
        </tr>
    </table>
    <input type="hidden" name="idNum" value="%s">
    <input type="hidden" name="lastname" value="%s">
    <input type="hidden" name="firstname" value="%s">
    </form>
    """ %fields
        


    
        
################################################################################    
def postStatusMessage(idNum, message):

    conn, cursor = getConnectionAndCursor()

    tm=time.localtime()
    timestamp= '%04d-%02d-%02d %02d:%02d:%02d' % tm[0:6]
    # prep some SQL
    sql = """
    INSERT INTO status VALUES
    (%s,%s,%s)

    """

    parameters=(timestamp,idNum,message)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount
################################################################################    
def addProfile(lastname,firstname,email,activities):

    conn, cursor = getConnectionAndCursor()

    sequel1= """
    SELECT max(id)
    FROM profiles
    """
    cursor.execute(sequel1)
    maxid=cursor.fetchone()
    maxid=maxid[0]+1
    
    # prep some SQL
    sql = """
    INSERT INTO profiles VALUES
    (%s,%s,%s,%s,%s)

    """

    parameters=(maxid,lastname,firstname,email,activities)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount

################################################################################


def updateProfile(idNum,email,activities):

    # connect to db
    conn, cursor = getConnectionAndCursor()

    
    # prep some SQL
    sql = """
    UPDATE profiles
    SET email=%s,
    activities=%s
    WHERE id=%s
    """

    parameters=(email,activities,idNum)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount
    

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount
################################################################################
def getFriends(idNum):

    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT *
    FROM friends
    WHERE id1=%s
    """

    # execute the query
    parameters = (int(idNum), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data

################################################################################
def showFriends(idNum,data):

    print """
    <h2>Friends List</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>lastname</b></font></td>
        <td><font size=+1"><b>firstname</b></font></td>
      </tr>
    """
    
    for row in data:

        # each iteration of this loop creates on row of output:
        (id1,id2) = row
        idNum=id2

        data=getOneProfile(idNum)
        
        for row in data:

        # each iteration of this loop creates on row of output:
            (idNum, lastname, firstName,email,activities) = row

            print """
          <tr>
            <td><a href="?idNum=%s">%s</a></td>
            <td><a href="?idNum=%s">%s</a></td>
          </tr>
            """ % (idNum, lastname, idNum, firstName,)

    print """
    </table>
    """
################################################################################
def addFriend(idNum, friendID):


    conn, cursor = getConnectionAndCursor()


    # prep some SQL
    sql = """
    INSERT INTO friends VALUES
    (%s,%s)

    """

    parameters=(idNum, friendID )

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount
    
################################################################################   
def getNewsFeed(idNum):


    conn, cursor = getConnectionAndCursor()

    # build SQL
    sql = """
    SELECT s.Message, s.DateTime, p.lastname, p.firstname
    FROM friends f, status s, profiles p
    WHERE f.id1=%s AND f.id2=s.id AND p.id=s.id
    ORDER BY DateTime DESC
    """

    # execute the query
    parameters = (int(idNum), )
    cursor.execute(sql, parameters)

    # get the data from the database:
    data = cursor.fetchall()

    # clean up
    conn.close()
    cursor.close()

    return data
################################################################################
def showNewsFeed(data):

    print """
    <h2>News Feed</h2>
    <p>
    
    <table border=1>
      <tr>
        <td><font size=+1"><b>Message</b></font></td>
        <td><font size=+1"><b>Date</b></font></td>  
        <td><font size=+1"><b>lastname</b></font></td>
        <td><font size=+1"><b>firstname</b></font></td>
      </tr>
    """
    for row in data:
        
        (Message, DateTime,lastname,firstname) = row


        print """
      <tr>
        <td><a href="?idNum=%s">%s</a></td>
        <td><a href="?idNum=%s">%s</a></td>
        <td><a href="?idNum=%s">%s</a></td>
        <td><a href="?idNum=%s">%s</a></td>
      </tr>
        """ % (idNum,Message,idNum,DateTime,idNum, lastname, idNum, firstname,)


    
    print """
    </table>
    """
        


################################################################################
if __name__ == "__main__":

    # get form field data
    form = cgi.FieldStorage()
    print form
    
    doHTMLHead("MiniFacebook")

    if "beginUpdate" in form:
        idNum=form["idNum"].value
        data= getOneProfile(idNum)
        showUpdateProfileForm(data)

        print data

    elif "updateprofile" in form:
        idNum=form["idNum"].value
        email=form["email"].value
        activities=form["activities"].value

        rowcount= updateProfile(idNum,email,activities)

        print "%d rows were updated.<p>" % rowcount


    elif "idNum" in form:
        idNum=form["idNum"].value
        data=getOneProfile(idNum)
        showProfilePage(data)


        if "post" in form:
            message=form["message"].value
            postStatusMessage(idNum, message)

        elif "addfriend" in form:
            friendID=form["friendID"].value
            addFriend(idNum, friendID)
            print "<B> friend added!</b>"
            



        
            
    elif "insertprofile" in form:

        lastname=form["lastname"].value
        firstname=form["firstname"].value
        email=form["email"].value
        activities=form["activities"].value

        rowcount=addProfile(lastname,firstname,email,activities)
        print "<B> profile added</b>"


       
        

    else:
#       profileForm()
        
        data = getAllUsers()
        showAllUsers(data)
        showAddProfileForm()



    doHTMLTail()    





