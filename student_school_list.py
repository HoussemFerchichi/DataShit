# ECOR 1042 Lab 3 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your student_school_list function after this line
def student_school_list(file_name: str, school: str) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the school field by reading a CSV file from a given file_name and filtering students by a given school.

    Precondition: (len(file_name) != 0) and (".csv" in file_name) and len(school) == 2
    

    >>> students = student_school_list("student-mat.csv","MS")
    >>> len(students)
    76
    >>> students[0]
    {'ID': 320, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}

    
    >>> students = student_school_list("student-mat.csv","GP")
    >>> len(students)
    79
    >>> students[0]
    {'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Failures': 0, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}


    >>> students = student_school_list("student-mat.csv","XX")
    >>> len(students)
    0
    >>> students
    []

    >>> student_school_list("student-mat.csv","MS")
    [{'ID': 320, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 321, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 23, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 322, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 12, 'FallGrade': 11, 'WinterGrade': 9}, {'ID': 323, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 3, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 324, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 1, 'FallGrade': 12, 'WinterGrade': 14}, {'ID': 325, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 2, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 326, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 3, 'FallGrade': 9, 'WinterGrade': 12}, {'ID': 327, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 15}, {'ID': 328, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 8, 'FallGrade': 11, 'WinterGrade': 10}, {'ID': 329, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 7, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 330, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 4, 'FallGrade': 14, 'WinterGrade': 14}, {'ID': 331, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 9, 'WinterGrade': 8}, {'ID': 332, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 7, 'FallGrade': 12, 'WinterGrade': 14}, {'ID': 333, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 0}, {'ID': 334, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 8}, {'ID': 335, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 336, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 16, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 337, 'Age': 19, 'StudyTime': 3.0, 'Failures': 1, 'Health': 5, 'Absences': 12, 'FallGrade': 14, 'WinterGrade': 13}, {'ID': 338, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 8}, {'ID': 339, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 340, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 9, 'WinterGrade': 10}, {'ID': 341, 'Age': 19, 'StudyTime': 3.0, 'Failures': 1, 'Health': 3, 'Absences': 4, 'FallGrade': 11, 'WinterGrade': 12}, {'ID': 342, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 2, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 343, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 11, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 344, 'Age': 17, 'StudyTime': 2.0, 'Failures': 1, 'Health': 4, 'Absences': 0, 'FallGrade': 9, 'WinterGrade': 8}, {'ID': 345, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 11, 'WinterGrade': 10}, {'ID': 346, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 7, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 347, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 9, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 348, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 349, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 13, 'WinterGrade': 15}, {'ID': 350, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 10, 'FallGrade': 11, 'WinterGrade': 13}, {'ID': 351, 'Age': 19, 'StudyTime': 2.0, 'Failures': 3, 'Health': 2, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 7}, {'ID': 352, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 353, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 3, 'Absences': 7, 'FallGrade': 8, 'WinterGrade': 7}, {'ID': 354, 'Age': 19, 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 8}, {'ID': 355, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 13, 'WinterGrade': 11}, {'ID': 356, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 357, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 4, 'FallGrade': 12, 'WinterGrade': 13}, {'ID': 358, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 2, 'FallGrade': 12, 'WinterGrade': 12}, {'ID': 359, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 360, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 18, 'WinterGrade': 16}, {'ID': 361, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 362, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 2, 'FallGrade': 13, 'WinterGrade': 12}, {'ID': 363, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 364, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 15}, {'ID': 365, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 0, 'FallGrade': 12, 'WinterGrade': 11}, {'ID': 366, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 367, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 13, 'WinterGrade': 13}, {'ID': 368, 'Age': 17, 'StudyTime': 1.0, 'Failures': 1, 'Health': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 6}, {'ID': 369, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 4, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 10}, {'ID': 370, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 5, 'Absences': 10, 'FallGrade': 14, 'WinterGrade': 12}, {'ID': 371, 'Age': 19, 'StudyTime': 2.0, 'Failures': 2, 'Health': 3, 'Absences': 4, 'FallGrade': 7, 'WinterGrade': 7}, {'ID': 372, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 3, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 12}, {'ID': 373, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Health': 3, 'Absences': 8, 'FallGrade': 13, 'WinterGrade': 11}, {'ID': 374, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 1, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 375, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 19, 'WinterGrade': 18}, {'ID': 376, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}, {'ID': 377, 'Age': 20, 'StudyTime': 3.0, 'Failures': 2, 'Health': 3, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'ID': 378, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 9}, {'ID': 379, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 15, 'WinterGrade': 15}, {'ID': 380, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 17, 'FallGrade': 10, 'WinterGrade': 10}, {'ID': 381, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 2, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'ID': 382, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 5, 'FallGrade': 7, 'WinterGrade': 6}, {'ID': 383, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Health': 3, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 11}, {'ID': 384, 'Age': 19, 'StudyTime': 1.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 385, 'Age': 18, 'StudyTime': 1.0, 'Failures': 1, 'Health': 3, 'Absences': 14, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 386, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Health': 4, 'Absences': 2, 'FallGrade': 10, 'WinterGrade': 9}, {'ID': 387, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 7, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 388, 'Age': 19, 'StudyTime': 3.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 5}, {'ID': 389, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Health': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 9}, {'ID': 390, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Health': 5, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'ID': 391, 'Age': 20, 'StudyTime': 2.0, 'Failures': 2, 'Health': 4, 'Absences': 11, 'FallGrade': 9, 'WinterGrade': 9}, {'ID': 392, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Health': 2, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 16}, {'ID': 393, 'Age': 21, 'StudyTime': 1.0, 'Failures': 3, 'Health': 3, 'Absences': 3, 'FallGrade': 10, 'WinterGrade': 8}, {'ID': 394, 'Age': 18, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 11, 'WinterGrade': 12}, {'ID': 395, 'Age': 19, 'StudyTime': 1.0, 'Failures': 0, 'Health': 5, 'Absences': 5, 'FallGrade': 8, 'WinterGrade': 9}]

    """
    # Get the index of StudyTime by searching and storing the index of first float element and exiting the loop to save memory usage and runtime (StudyTime is the only float element assuming like instructed that the data is in the correct format).
    # We implemented this method for the reason that the file can contain StudyTime value as an int so we can't convert it depending on the type it was stored in and assuming that the key could have a different name and index each time we need to fetch it dynamically.
    file = open(file_name,"r")
    studytime_index = -1
    for line in file:
        keys = line.strip().split(",")
        for item in keys:
            try:
                if (item.index(".")>-1) and str(float(item)) == str(item): # checking if the item is a float .
                    studytime_index = keys.index(item) 
                    break   # Saving the list index of the first float element and breaking out of the loop.
            except:studytime_index = -1 # Pass the Statement if we got any non float items (we're not sure if we can use Pass).
        if studytime_index != -1 : break # Breaking out of the loop for the first float found with its index saved in studytime_index.
    file.close()
    # Closing and re-opening the file to reset the pointer as we can't use seek().
    file = open(file_name,"r")
    # Initializing the filter_key and the filter_str(value) that we're only saving the students with those conditions.
    filter_key = "School"
    filter_str = str(school)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        print(keys)
        break
    # Filtering and saving the students according to their school. 
    data=[]
    for line in file:
        header = {key : list for key in keys} # Creating the dictionary with the list keys assigning each key value to a new item with the key name from the list keys and making sure it reset the dictionary each loop.
        values = line.strip().split(",") # Creating a list with no white spaces that contains the list values fetched from the file.
        if values[keys.index(filter_key)]==filter_str: # Condition to check if the current line we're pointing on in the file is meeting the conditions of our filter.
            for i in range(len(values)): # Looping through the values of the list.
                if i != keys.index(filter_key): # Making sure not to save the value for the key that we're filtering to save memory.
                    # Saving the values with their correct data type if it's study time then save it as a float otherwise try to save it as an it if it failed then save it as a string
                    try:
                        if i == studytime_index :header[keys[i]]=float(values[i])
                        else : header[keys[i]]=int(values[i])
                    except : header[keys[i]]=values[i]
            header.pop(filter_key) # Removing the item that we filtered with.
            data.append(header) # Add the data saved from the dictionary into a new item into the data list
    # Closing the file and returning the filtered students
    file.close()
    return data

# Do NOT include a main script in your submission
