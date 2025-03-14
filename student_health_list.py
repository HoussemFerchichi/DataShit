# ECOR 1042 Lab 3 - Individual submission for student_health_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your student_health_list function after this line
def student_health_list(file_name: str, health: int) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the health field by reading a CSV file from a given file_name and filtering students by a given health.

    Precondition: (len(file_name) != 0) and (".csv" in file_name) and health >= 1 and health <=5
    

    >>> students = student_health_list("student-mat.csv",1)
    >>> len(students)
    47
    >>> students[0]
    {'School': 'GP', 'ID': 8, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 6, 'WinterGrade': 5}

    
    >>> students = student_health_list("student-mat.csv",5)
    >>> len(students)
    146
    >>> students[0]
    {'School': 'GP', 'ID': 4, 'Age': 15, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 15, 'WinterGrade': 14}


    >>> students = student_health_list("student-mat.csv",2)
    >>> len(students)
    45
    >>> student_health_list("student-mat.csv",2)
    [{'School': 'GP', 'ID': 11, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 8}, {'School': 'GP', 'ID': 16, 'Age': 16, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 14, 'WinterGrade': 14}, {'School': 'GP', 'ID': 17, 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 13, 'WinterGrade': 14}, {'School': 'GP', 'ID': 34, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 10}, {'School': 'GP', 'ID': 40, 'Age': 15, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 8, 'FallGrade': 14, 'WinterGrade': 13}, {'School': 'GP', 'ID': 48, 'Age': 16, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 19, 'WinterGrade': 19}, {'School': 'GP', 'ID': 56, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'GP', 'ID': 65, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'MB', 'ID': 87, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'MB', 'ID': 93, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 7, 'WinterGrade': 6}, {'School': 'MB', 'ID': 104, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 26, 'FallGrade': 7, 'WinterGrade': 6}, {'School': 'MB', 'ID': 112, 'Age': 16, 'StudyTime': 3.0, 'Failures': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 10}, {'School': 'MB', 'ID': 117, 'Age': 15, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 11, 'WinterGrade': 13}, {'School': 'MB', 'ID': 142, 'Age': 16, 'StudyTime': 1.0, 'Failures': 2, 'Absences': 8, 'FallGrade': 9, 'WinterGrade': 9}, {'School': 'CF', 'ID': 164, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'CF', 'ID': 166, 'Age': 16, 'StudyTime': 1.0, 'Failures': 1, 'Absences': 16, 'FallGrade': 12, 'WinterGrade': 11}, {'School': 'CF', 'ID': 171, 'Age': 16, 'StudyTime': 1.0, 'Failures': 2, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'CF', 'ID': 180, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'CF', 'ID': 191, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 10, 'FallGrade': 11, 'WinterGrade': 12}, {'School': 'CF', 'ID': 199, 'Age': 17, 'StudyTime': 1.0, 'Failures': 1, 'Absences': 24, 'FallGrade': 18, 'WinterGrade': 18}, {'School': 'CF', 'ID': 201, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 2, 'FallGrade': 16, 'WinterGrade': 16}, {'School': 'CF', 'ID': 233, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 14, 'FallGrade': 11, 'WinterGrade': 9}, {'School': 'CF', 'ID': 236, 'Age': 16, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 10, 'FallGrade': 11, 'WinterGrade': 9}, {'School': 'BD', 'ID': 240, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 7}, {'School': 'BD', 'ID': 247, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 12, 'WinterGrade': 12}, {'School': 'BD', 'ID': 252, 'Age': 16, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 7, 'WinterGrade': 10}, {'School': 'BD', 'ID': 260, 'Age': 17, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'School': 'BD', 'ID': 261, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 21, 'FallGrade': 17, 'WinterGrade': 18}, {'School': 'BD', 'ID': 272, 'Age': 18, 'StudyTime': 4.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'BD', 'ID': 287, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 5, 'FallGrade': 18, 'WinterGrade': 18}, {'School': 'BD', 'ID': 289, 'Age': 18, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 6, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'BD', 'ID': 290, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 9, 'FallGrade': 15, 'WinterGrade': 13}, {'School': 'BD', 'ID': 297, 'Age': 19, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 9}, {'School': 'BD', 'ID': 298, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 10, 'FallGrade': 10, 'WinterGrade': 8}, {'School': 'BD', 'ID': 312, 'Age': 19, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 20, 'FallGrade': 14, 'WinterGrade': 12}, {'School': 'MS', 'ID': 325, 'Age': 17, 'StudyTime': 3.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 16, 'WinterGrade': 15}, {'School': 'MS', 'ID': 334, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 8}, {'School': 'MS', 'ID': 338, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 0, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'MS', 'ID': 340, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 9, 'WinterGrade': 10}, {'School': 'MS', 'ID': 342, 'Age': 18, 'StudyTime': 2.0, 'Failures': 1, 'Absences': 0, 'FallGrade': 10, 'WinterGrade': 10}, {'School': 'MS', 'ID': 351, 'Age': 19, 'StudyTime': 2.0, 'Failures': 3, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'MS', 'ID': 355, 'Age': 17, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 13, 'WinterGrade': 11}, {'School': 'MS', 'ID': 378, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'MS', 'ID': 381, 'Age': 18, 'StudyTime': 2.0, 'Failures': 0, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'MS', 'ID': 392, 'Age': 17, 'StudyTime': 1.0, 'Failures': 0, 'Absences': 3, 'FallGrade': 14, 'WinterGrade': 16}]
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
    filter_key = "Health"
    filter_str = str(health)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their health. 
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
