# ECOR 1042 Lab 5 - Individual submission for sort_students_age_bubble

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Houssem Ferchichi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101344983"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your sort_students_age_bubble function after this line


# Do NOT include a main script in your submission

def sort_students_age_bubble(students, order):
    if not students:
        return "Empty list."
    
    if not all("Age" in student for student in students):
        return "List not sorted. Age key not present."
    
    n = len(students)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (order == "A" and students[j]["Age"] > students[j + 1]["Age"]) or \
               (order == "D" and students[j]["Age"] < students[j + 1]["Age"]):
                students[j], students[j + 1] = students[j + 1], students[j]
    
    return "List sorted."


