# miniFB.py
#
# Author: Aaron Stevens (azs@bu.edu), YOUR NAME HERE
#
# Description:
# a simple application which simulates the core social networking
# features of Facebook:
#   creating/updating user profiles;
#   adding friends;
#   creating and viewing status messages.

import time
import sqlite3 as db

#####################################################################################
def getDBConnectionAndCursor():
    """
    This helper function establishes a connection to the database and returns
    a valid connection and cursor object.
    """

    # connect to the database 
    pathname = "/Users/xiangormirko/Desktop/miniFB.db" # you might need to change this to suit your filesystem
    conn = db.connect(pathname)
    # obtain a cursor object
    cursor = conn.cursor()

    # return connection and cursor to calling context
    return conn, cursor

################################################################################
def displayUserList():
    """
    Displays a list of all users from the profiles database.
    """

    print
    print "Display user list."
    conn, cursor= getDBConnectionAndCursor()
    
    sql="""
    SELECT *
    FROM profiles
    """
    cursor.execute(sql)

    results= cursor.fetchall()
    for row in results:
        (id,lastname,firstname,email,activities)=row
        print "%s %s" % (firstname, lastname)

    conn.commit()
    cursor.close()
    conn.close
    ## Your Code Here!
    ## display a list of user id, firstname, lastname, email (no activities)

################################################################################
def showProfilePage():
    """
    Displays the profile page for a single user.
    """

    print
    print "Showing a profile page."

    idNum = input("Enter profile ID: ")
    conn, cursor= getDBConnectionAndCursor()


    sql= """
    SELECT *
    FROM profiles
    WHERE id=?
    """
    parameters= (idNum, )
    cursor.execute(sql, parameters)

    results=cursor.fetchall()
    for row in results:
        (id,lastname,firstname,email,activities)=row
        print "id %s, name %s. %s, email: %s, activities: %s" % (id, lastname,firstname,email,activities)

    conn.commit()
    cursor.close()
    conn.close
    ## Your Code Here!
    ## show the content of the profile for the record with idNum
    ## show all the fields in a decent format

    

################################################################################
def createProfile():
    """
    Create a new profile, and store the record in the profiles table.
    """

    print
    print "Create a new profile."
    firstName = raw_input("Enter First Name: ")
    lastName = raw_input("Enter Last Name: ")
    email = raw_input("Enter Email Address: ")
    activities = raw_input("Enter Activities: ")
    conn, cursor= getDBConnectionAndCursor()

 #   """sql1="""
###    SELECT MAX(id)
 #   FROM profiles
 #   """
 #   cursor.execute(sql1)
 #   idmax= cursor.fetchall()

 #   integer= int(idmax[0])

 #   newid=integer+1"""
    
    sql="""
    INSERT INTO profiles
    VALUES('%s','%.s','%s','%s','%s')
    """ %(7,lastName,firstName,email,activities)
    

    cursor.execute(sql)

    
    conn.commit()
    cursor.close()
    conn.close
    ## Your Code Here!
    ## insert a new record into the database with this info.
    ## make sure you find the next unused idNum before inserting.

    

################################################################################
def updateProfile():
    """
    Update a profile, to change the email or activities.
    """

    print
    print "Update a profile."

    idNum = input("Enter profile ID: ")
    email = raw_input("Enter Email Address: ")
    activities = raw_input("Enter Activities: ")
    conn, cursor= getDBConnectionAndCursor()

    sql="""
    UPDATE profiles
    SET email=?, activities=?
    WHERE id=?
    """
    parameters=(email,activities,idNum)
    cursor.execute(sql,parameters)


    rowcount= cursor.rowcount
    print "%d records were affected by this update." %rowcount

    if rowcount==1:
        conn.commit()

    else:
        print "The rowcount was unexpected, so no changes were committed."
    cursor.close()
    conn.close    
    ## Your Code Here!
    ## make update to the database for the record with idNum


################################################################################
def showFriends():
    """
    Displays a list of all friends for a single user.
    """

    print
    print "Show friends."

    idNum = input("For whom to list friends? Enter profile ID: ")
    conn, cursor= getDBConnectionAndCursor()

    sql="""
    SELECT id2
    FROM friends
    WHERE id1=?
    """
    parameters=( idNum,)
    cursor.execute(sql,parameters)

    results=cursor.fetchall()
    
    for num in results:
        sql2="""
        SELECT firstname,lastname
        FROM profiles
        WHERE id=?
        """
        parameters1=(num,)
        cursor.execute(sql2,parameters1)

        result=cursor.fetchall()
        print result

    
    conn.commit()
    cursor.close()
    conn.close   
    ## Your Code Here!
    ## Query 'friends' table to find all friends's idNumbers for this idNum


    ## For each friend's idNum, query 'profiles' table to lastname, firstname


################################################################################
def addFriend():
    """
    Add (create) a friend relationship between two users.
    """

    print
    print "Add a friend."

    idNum = input("Who is adding the friend? Enter profile ID: ")
    friendID = input("Who is the friend? Enter profile ID: ")
    conn, cursor= getDBConnectionAndCursor()

    sql="""
    INSERT INTO friends
    VALUES (%d, %d)
    """ %(idNum, friendID)

    cursor.execute(sql)
    

    
    conn.commit()
    cursor.close()
    conn.close     
    ## Your Code Here!
    ## insert a record to friends table with both ID numbers


################################################################################
def showStatusMessages():
    """
    Displays a list of status messages for a single user's friends.
    """

    print
    print "Show status messages."

    idNum = input("For whom should we find status updates? Enter a profile ID: ")
    conn, cursor= getDBConnectionAndCursor()

    sql="""
    SELECT *
    FROM status
    WHERE id=?
    """
    parameters=(idNum, )
    cursor.execute(sql, parameters)
    results=cursor.fetchall()
    for row in results:
        (date,idNum,message)=row
        print " Date: %s, id: %s, message: %s" %(date,idNum,message)

    
    conn.commit()
    cursor.close()
    conn.close 
    ## Your Code Here!
    ## Query 'friends' table to find all friends's idNumbers for this idNum


    ## For each friend's idNum:
    ## (1) query 'profiles' table to lastname, firstname
    ## (2) query 'status' table to find all status updates for friend's idNum

    

    
################################################################################
def writeStatusMessage():
    """
    Compose a new status message and record it to the status table..
    """

    print
    print "Write a status message."

    idNum = input("Who is writing the status message? Enter a profile ID: ")
    message = raw_input("What are you doing right now? ")

    tm = time.localtime()
    nowtime = '%04d-%02d-%02d %02d:%02d:%02d' % tm[0:6]
    conn, cursor= getDBConnectionAndCursor()

    sql="""
    INSERT INTO status
    VALUES(%s, %s, %s)
    """ %(nowtime, idNum, message)

    cursor.execute(sql)
    

    conn.commit()
    cursor.close()
    conn.close 
    ## Your Code Here!
    ## do an insert into the status table with this status message

    

################################################################################
if __name__ == "__main__":

    # a main program loop:

    choice = "foo"

    while choice.lower()[0] != "q":

        print """
    MiniFacebook: Please select an option:
    (d) display user list       (f) show friends
    (p) show profile page       (a) add friend
    (c) create profile          (s) show status messages
    (u) update profile          (w) write status message
    (q) quit the application
    """
        
        choice = raw_input("> ")

        if choice.lower()[0] == "d":

            displayUserList()
            
        elif choice.lower()[0] == "p":

            showProfilePage()

        elif choice.lower()[0] == "c":

            createProfile()

        elif choice.lower()[0] == "u":

            updateProfile()

        elif choice.lower()[0] == "f":

            showFriends()

        elif choice.lower()[0] == "a":

            addFriend()

        elif choice.lower()[0] == "s":

            showStatusMessages()

        elif choice.lower()[0] == "w":

            writeStatusMessage()

        # end of the loop

print "Goodbye!"
        
