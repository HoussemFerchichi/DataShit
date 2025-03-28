# ECOR 1042 Lab 5 - Individual submission for sort_students_time_selection function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Brett Patzer"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101323409"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your sort_students_time_selection function after this line


# Do NOT include a main script in your submission

def sort_students_time_selection(students, order):
    if not students:
        return "Empty list."
    
    if not all("StudyTime" in student for student in students):
        return "List not sorted. StudyTime key not present."
    
    n = len(students)
    ascending = order == "A"
    
    for i in range(n):
        extreme_idx = i
        for j in range(i + 1, n):
            if (ascending and students[j]["StudyTime"] < students[extreme_idx]["StudyTime"]) or \
               (not ascending and students[j]["StudyTime"] > students[extreme_idx]["StudyTime"]):
                extreme_idx = j
        
        students[i], students[extreme_idx] = students[extreme_idx], students[i]
    
    return "List sorted."


