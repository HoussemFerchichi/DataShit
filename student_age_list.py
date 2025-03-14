# ECOR 1042 Lab 3 - Individual submission for student_age_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your student_age_list function after this line
def student_age_list(file_name: str, age: int) -> list[dict[str, str]]:
    """return a list of dictionaries where each dictionary represents a student and their corresponding details excluding the age field by reading a CSV file from a given file_name and filtering students by a given age.

    Precondition: (len(file_name) != 0) and (".csv" in file_name) and age >= 10 and age <= 25
    

    >>> students = student_age_list("student-mat.csv",15)
    >>> len(students)
    82
    >>> students[0]
    {'School': 'GP', 'ID': 3, 'StudyTime': 2, 'Failures': 3, 'Health': 3, 'Absences': 10, 'FallGrade': 7, 'WinterGrade': 8}

    
    >>> students = student_age_list("student-mat.csv",17)
    >>> len(students)
    98
    >>> students[0]
    {'School': 'GP', 'ID': 2, 'StudyTime': 2, 'Failures': 0, 'Health': 3, 'Absences': 4, 'FallGrade': 5, 'WinterGrade': 5}


    >>> students = student_age_list("student-mat.csv",23)
    >>> len(students)
    0
    >>> students
    []

    >>> students = student_age_list("student-mat.csv",20)
    >>> len(students)
    3
    >>> students
    [{'School': 'BD', 'ID': 307, 'StudyTime': 1, 'Failures': 0, 'Health': 5, 'Absences': 0, 'FallGrade': 17, 'WinterGrade': 18}, {'School': 'MS', 'ID': 377, 'StudyTime': 3, 'Failures': 2, 'Health': 3, 'Absences': 4, 'FallGrade': 15, 'WinterGrade': 14}, {'School': 'MS', 'ID': 391, 'StudyTime': 2, 'Failures': 2, 'Health': 4, 'Absences': 11, 'FallGrade': 9, 'WinterGrade': 9}]
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
    filter_key = "Age"
    filter_str = str(age)
    # Going through the file and breaking after the first line which contains the header and we save it into a list to create the dictionary with the names in the list
    for line in file:
        keys = line.strip().split(",")
        break
    # Filtering and saving the students according to their age. 
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
