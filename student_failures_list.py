# ECOR 1042 Lab 3 - Individual submission for student_failures_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(file_name: str, failures: int) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the failures field by reading a CSV file from a given file_name and filtering students by a given failures.

    Precondition: (len(file_name) != 0) and (".csv" in file_name) and failures >= 0
    

    >>> students = student_failures_list("student-mat.csv",0)
    >>> len(students)
    312
    >>> students[0]
    {'School': 'GP', 'ID': 1, 'Age': 18, 'StudyTime': 2.5, 'Health': 3, 'Absences': 6, 'FallGrade': 5, 'WinterGrade': 6}

    
    >>> students = student_failures_list("student-mat.csv",3)
    >>> len(students)
    16
    >>> students
    [{'School': 'GP', 'ID': 3, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'GP', 'ID': 19, 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 16, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'GP', 'ID': 79, 'Age': 17, 'StudyTime': 1.0, 'Health': 3, 'Absences': 2, 'FallGrade': 8, 'WinterGrade': 8}, {'School': 'MB', 'ID': 128, 'Age': 19, 'StudyTime': 2.0, 'Health': 5, 'Absences': 2, 'FallGrade': 7, 'WinterGrade': 8}, {'School': 'MB', 'ID': 145, 'Age': 17, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'FallGrade': 5, 'WinterGrade': 0}, {'School': 'MB', 'ID': 147, 'Age': 15, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 7}, {'School': 'MB', 'ID': 150, 'Age': 15, 'StudyTime': 1.0, 'Health': 5, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 9}, {'School': 'MB', 'ID': 151, 'Age': 18, 'StudyTime': 1.0, 'Health': 4, 'Absences': 0, 'FallGrade': 6, 'WinterGrade': 5}, {'School': 'MB', 'ID': 154, 'Age': 19, 'StudyTime': 1.0, 'Health': 4, 'Absences': 0, 'FallGrade': 5, 'WinterGrade': 0}, {'School': 'MB', 'ID': 158, 'Age': 18, 'StudyTime': 1.0, 'Health': 4, 'Absences': 6, 'FallGrade': 9, 'WinterGrade': 8}, {'School': 'CF', 'ID': 165, 'Age': 17, 'StudyTime': 2.0, 'Health': 5, 'Absences': 0, 'FallGrade': 5, 'WinterGrade': 8}, {'School': 'CF', 'ID': 174, 'Age': 16, 'StudyTime': 2.0, 'Health': 3, 'Absences': 0, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'CF', 'ID': 207, 'Age': 16, 'StudyTime': 2.0, 'Health': 4, 'Absences': 5, 'FallGrade': 7, 'WinterGrade': 7}, {'School': 'BD', 'ID': 248, 'Age': 22, 'StudyTime': 1.0, 'Health': 1, 'Absences': 16, 'FallGrade': 6, 'WinterGrade': 8}, {'School': 'MS', 'ID': 351, 'Age': 19, 'StudyTime': 2.0, 'Health': 2, 'Absences': 8, 'FallGrade': 8, 'WinterGrade': 7}, {'School': 'MS', 'ID': 393, 'Age': 21, 'StudyTime': 1.0, 'Health': 3, 'Absences': 3, 'FallGrade': 10, 'WinterGrade': 8}]

    >>> students = student_failures_list("student-mat.csv",4)
    >>> len(students)
    0
    >>> students
    []
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
    filter_key = "Failures"
    filter_str = str(failures)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their failures. 
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
