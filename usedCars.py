#!/usr/bin/python
#
# file: usedCars.py
# Author: Mirko (xiang@bu.edu)
# Description: demonstrate a LAMP-type program with Python script
#               connecting to a MySQL database.
#

import MySQLdb as db
import time
import cgi
import cgitb; cgitb.enable()

print "Content-Type: text/html"
print "" # blank line

################################################################################
def getConnectionAndCursor():
    """
    This function will connect to the database and return the
    Connection and Cursor objects.
    """

    # SQLite version had these lines, which we do not need for MySQL.
    # path = "/..."
    #conn = db.connect(path)
    
    # connect to the MYSQL database
    conn = db.connect(host="localhost",
                      user="readonlyuser",
                      passwd="readonly",
                      db="examples")

    cursor = conn.cursor()
    return conn, cursor

################################################################################
def doHTMLHead(title):

    print """
    <html>
    <head>
    <title>%s</title>
    <body>
    <h1>%s</h1>

    <p>
    """ % (title, title)

################################################################################
def doHTMLTail():

    print """
    <p>
    <hr>
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

################################################################################
def getAllCars():
    """
    This is a middleware function to read from the database.
    It returns a list containing records of all cars in the table.
    """
    
    # connect to db
    conn, cursor = getConnectionAndCursor()
    
    # prep some SQL
    sql = """
    SELECT *
    FROM usedcars
    """
    
    # run the SQL
    cursor.execute(sql)
    
    # fetch the results
    data = cursor.fetchall()

    # clean up
    cursor.close()
    conn.close()
    
    return data

## end: def getAllCars()


################################################################################
def getAllCarsByMake(make):
    """
    This is a middleware function to read from the database.
    It returns a list containing records of all cars of make.
    """
    
    # connect to db
    conn, cursor = getConnectionAndCursor()
    
    # prep some SQL
    sql = """
    SELECT *
    FROM usedcars
    WHERE make=%s
    """

    parameters=(make, )

    cursor.execute(sql,parameters)
    

    
    # fetch the results
    data = cursor.fetchall()

    # clean up
    cursor.close()
    conn.close()
    
    return data

## end: def getAllCars()

################################################################################
def getOneCar(vin):
    """
    This is a middleware function to read from the database.
    It returns a list containing records of all cars of make.
    """
    
    # connect to db
    conn, cursor = getConnectionAndCursor()
    
    # prep some SQL
    sql = """
    SELECT *
    FROM usedcars
    WHERE vin=%s
    """

    parameters=(vin, )

    cursor.execute(sql,parameters)
    

    
    # fetch the results
    data = cursor.fetchall()

    # clean up
    cursor.close()
    conn.close()
    
    return data



##############################################################################
def printMainMenu():


    print """
    <form>

        <input type="submit" name="showAllCars" value="Show all Cars">
    </form>
    """


    print """

    <form>
    <select name="make">
        <option value="Acura">Acura</option>
        <option value="BMW">BMW</option>
        <option value="Chevrolet">Chevrolet</option>
        <option value="Ford">Ford</option>
        <option value="Honda">Honda</option>
        <option value="HUMMER">HUMMER</option>
        <option value="Land Rover">Land Rover</option>
        <option value="Lexus">Lexus</option>
        <option value="Mazda">Mazda</option>
        <option value="Mercedes-Benz">Mercedes-Benz</option>
        <option value="Nissan">Nissan</option>
        <option value="Saab">Saab</option>
        <option value="Subaru">Subaru</option>
        <option value="Porsche">Porsche</option>
        <option value="Toyota">Toyota</option>
        <option value="Volkswagen">Volkswagen</option>
    </select>
    <input type="submit" name="searchByMake" value="Search">
    </form>
    """

    print """
    <form>

        <input type="submit" name="showAddCarForm" value="Add A Car">
    </form>
    """




    
## end def printSelectMakeForm() 
################################################################################      
def pintOutCars(data):
    print """
    <table>
        <tr>
            <td>Vin</td>
            <td>Year</td>
            <td>Make</td>
            <td>Model</td>
            <td>Doors</td>
            <td>Type</td>
            <td>Mileage</td>
            <td>HWMPG</td>
            <td>CITYMPG</td>
            <td>Price</td>
            <td>Action</td>
        <tr>
        """

    for record in data:

        vin= record[0]
        fields= record +(vin,)
        print"""
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td>
            <form>
                <input type="submit" name="beginUpdateCar" value="update">
                <input type="hidden" name="vin" value="%s">
            </form>
            </td>
        <tr>
        """ % fields
        


    print """
    </table>
    """

################################################################################
def printSelectMakeForm():

    print """
    <h2>Search cars by make</h2>
    <p>
    <form>
    <select name="make">
        <option value= "Acura">Acura</option>
        <option value= "BMW">BMW</option>
        <option value= "Acura">Acura</option>
        <option value= "Chevrolet">Chevrolet</option>
        <option value= "Ford">Ford</option>
        <option value= "Honda">Honda</option>
        <option value= "HUMMER">HUMMER</option>
        <option value= "Land Rover">Land Rover</option>
        <option value= "Lexus">Lexus</option>
        <option value= "Mazda">Mazda</option>
        <option value= "Mercedes-Benz">Mercedec-Benz</option>
        <option value= "Nissan">Nissan</option>
        <option value= "Saab">Saab</option>
        <option value= "Subaru">Subaru</option>
        <option value= "Porsche">Porsche</option>
        <option value= "Toyota">Toyota</option>
        <option value= "Volkswagen">Volkswagen</option>
    </select>



    <input type="submit" name="searchByMake" value="Search">
    </form>
    """
        


################################################################################
def printInsertCarForm():

    print """
    <form>
    <table>
        <tr>
            <td>Vin</td>
            <td><input type="text" name="vin"></td>
        </tr>
        <tr>
            <td>Year</td>
            <td><input type="text" name="year"></td>
        </tr>
        <tr>
            <td>Make</td>
            <td>
            <select name="make">            
                <option value= "Acura">Acura</option>
                <option value= "BMW">BMW</option>
                <option value= "Acura">Acura</option>
                <option value= "Chevrolet">Chevrolet</option>
                <option value= "Ford">Ford</option>
                <option value= "Honda">Honda</option>
                <option value= "HUMMER">HUMMER</option>
                <option value= "Land Rover">Land Rover</option>
                <option value= "Lexus">Lexus</option>
                <option value= "Mazda">Mazda</option>
                <option value= "Mercedes-Benz">Mercedec-Benz</option>
                <option value= "Nissan">Nissan</option>
                <option value= "Saab">Saab</option>
                <option value= "Subaru">Subaru</option>
                <option value= "Porsche">Porsche</option>
                <option value= "Toyota">Toyota</option>
                <option value= "Volkswagen">Volkswagen</option>
            </select>
            </td>
                    
        </tr>
        <tr>
            <td>Model</td>
            <td><input type="text" name="model"></td>
        </tr>
        <tr>
            <td>Doors</td>
            <td><input type="text" name="doors"></td>
        </tr>
        <tr>
            <td>Type</td>
            <td><input type="text" name="type"></td>
        </tr>
        <tr>
            <td>Mileage</td>
            <td><input type="text" name="mileage"></td>
        </tr>
        <tr>
            <td>HWMPG</td>
            <td><input type="text" name="hwmpg"></td>
        </tr>
        <tr>
            <td>CITYMPG</td>
            <td><input type="text" name="citympg"></td>
        </tr>
        <tr>
            <td>Price</td>
            <td><input type="text" name="price"></td>
        <tr>

        <tr>
            <td>

        <input type="submit" name="insertNewCar" value="Insert new Car">
        <input type="submit" name="cancel" value="Cancel Insert">
        </td>
            </td>
        </tr>
    </table>
    </form>
    """
################################################################################
def printUpdateCarForm(data):


    record= data[0]
    vin= record[0]
    make= record[2]
    fields= record+ (vin, make)
    
    print """

    <h2> Update Car Form</h2>
    <form>
    <table>
        <tr>
            <td>Vin</td>
            <td>%s</td>
        </tr>
        <tr>
            <td>Year</td>
            <td><input type="text" name="year" value="%s"></td>
        </tr>
        <tr>
            <td>Make</td>
            <td>%s</td>
                    
        </tr>
        <tr>
            <td>Model</td>
            <td><input type="text" name="model" value="%s"></td>
        </tr>
        <tr>
            <td>Doors</td>
            <td><input type="text" name="doors" value="%s"></td>
        </tr>
        <tr>
            <td>Type</td>
            <td><input type="text" name="type" value="%s"></td>
        </tr>
        <tr>
            <td>Mileage</td>
            <td><input type="text" name="mileage" value="%s"></td>
        </tr>
        <tr>
            <td>HWMPG</td>
            <td><input type="text" name="hwmpg" value="%s"></td>
        </tr>
        <tr>
            <td>CITYMPG</td>
            <td><input type="text" name="citympg" value="%s"></td>
        </tr>
        <tr>
            <td>Price</td>
            <td><input type="text" name="price" value="%s"></td>
        <tr>

        <tr>
            <td>

        <input type="submit" name="completeUpdateCar" value="Update Car">
        <input type="submit" name="cancel" value="Cancel Update">
        </td>
            </td>
        </tr>
    </table>
    <input type="hidden" name= "vin" value=%s">
    <input type="hidden" name= "make" value=%s">
    
    </form>
    """ % fields

    
################################################################################


def insertNewCar(vin, year, make, model, doors, carType, mileage, hwmpg, citympg, price):

    # connect to db
    conn, cursor = getConnectionAndCursor()
    
    # prep some SQL
    sql = """
    INSERT INTO usedcars VALUES
    (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

    """

    parameters=(vin, year, make, model, doors, carType, mileage, hwmpg, citympg, price)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount

################################################################################


def updateCar(vin, year, make, model, doors, carType, mileage, hwmpg, citympg, price):

    # connect to db
    conn, cursor = getConnectionAndCursor()
    
    # prep some SQL
    sql = """
    UPDATE usedcars
    SET year=%s,
    model=%s,
    doors=%s,
    type=%s,
    odometer=%s,
    hwmpg=%s,
    citympg=%s,
    price=%s,
    WHERE vin=%s


    """

    parameters=( year, model, doors, carType, mileage, hwmpg, citympg, price, vin)

    cursor.execute(sql,parameters)
    
    rowcount=cursor.rowcount

    


    # clean up
    conn.commit()
    cursor.close()
    conn.close()
    
    return rowcount

################################################################################

if __name__ == "__main__":
    """
    The main section of our program. The program always starts here,
    and work is delegated to other functions as appropriate.
    """

    doHTMLHead("Used Cars")

    # get the form data from the HTTP request
    form = cgi.FieldStorage() 
#    debugFormData(form)

    if "searchByMake" in form:

        make=form["make"].value
        data= getAllCarsByMake(make)
        pintOutCars(data)


    elif "showAllCars" in form:

        data = getAllCars()
        pintOutCars(data)
        
    elif "showAddCarForm" in form:
        printInsertCarForm()
        
    elif "insertNewCar" in form:
        vin=form["vin"].value
        year=form["year"].value
        make=form["make"].value
        model=form["model"].value
        doors=form["doors"].value
        carType=form["type"].value
        mileage=form["mileage"].value
        hwmpg=form["hwmpg"].value
        citympg=form["citympg"].value
        price=form["price"].value


        rowcount=insertNewCar(vin, year, make, model, doors, carType, mileage, hwmpg, citympg, price)

        if rowcount == 1:
            print "<B> insert succeeded</b>"

    elif "beginUpdateCar" in form:
        vin= form["vin"].value
        data=getOneCar(vin)

        print data
        printUpdateCarForm(data)

    elif "completeUpdateCar" in form:
        
        vin=form["vin"].value
        year=form["year"].value
        make=form["make"].value
        model=form["model"].value
        doors=form["doors"].value
        carType=form["type"].value
        mileage=form["mileage"].value
        hwmpg=form["hwmpg"].value
        citympg=form["citympg"].value
        price=form["price"].value

        rowcount= updateCar(vin, year, make, model, doors, carType, mileage, hwmpg, citympg, price)
        
        print "%d rows were updated.<p>" % rowcount

        
    
    else:
        printMainMenu()

    # TO DO: read data from database, print out results...
    
    print """
<a href="./usedCars.py">Return to main screen</a>
    """
    doHTMLTail()


