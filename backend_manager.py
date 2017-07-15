import MySQLdb as mysql

def db_link(db_name, table_name, username, passwrd):
    '''
    Connects to the database whose name, access username, and password have been 
    provided on the web app and have been fed into the function.

    Returns a tuple of all rows of the specified table, each of which is a tuple.

    Input assumptions: all input values are string values
    '''
    #Create the database object and connect.
    #Assumption that database is hosted on local server with standard mySQL port
    db = mysql.connect(host="127.0.0.1", port=3306, user=username, passwd=passwrd, db=db_name)
    #Create a cursor object to help read the database
    c = db.cursor()
    #Write the command to fetch all rows from the database
    extract_command = "select * from %s", table_name
    #Execute the command using the cursor
    c.execute(extract_command)
    return c.fetchall()


def pass_to_classifier(dataset):
    '''
    Takes in the the dataset represented as a collection of rows.

    Returns another tuple with class values at corresponding indexes of dataset rows.

    Input assumption: dataset is a tuple composed of individual tuples each of whch
                      represents a row
    '''
    #Create a list for the output values
    output_classes = []
    numEntries = len(dataset)
    #Loop through each of the individual tuples in the dataset megatuple
    for tuple_index in range(numEntries):
        #Each input row has only one column comprising the text, so just feed that
        #into the classifier function.
        classifier_input = dataset[0][0]
        output = #replace with classifier function
        output_classes[tuple_index] = output
    #Loop through each of the output values and put them in the same row as the input
    for list_index in range(numEntries):
        corr_input = dataset[list_index][0]
        insert_command = 
        
