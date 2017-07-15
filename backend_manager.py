import MySQLdb as mysql

def db_link(db):
    '''
    Connects to the database whose connection has been fed to the function.

    Returns a tuple of all rows of the specified table, each of which is a tuple.
    '''
    #Create a cursor object to help read the database
    c = db.cursor()
    #Write the command to fetch all rows from the database
    extract_command = "select * from %s", db_names[1]
    #Execute the command using the cursor
    c.execute(extract_command)
    return c.fetchall()


def pass_to_classifier(dataset, table_name):
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
        output = predict
        output_classes[tuple_index] = output
    #Loop through each of the output values and put them in the same row as the input
    for list_index in range(numEntries):
        output2 = output_classes[list_index]
        corr_input = dataset[list_index][0]
        insert_command = "update %s set classification=%d where input_text=%s" %(table_name, output2, corr_input)
        c.execute(insert_command)
