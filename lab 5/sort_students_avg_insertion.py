# ECOR 1042 Lab 5 - Individual submission for sort_students_avg_insertion function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Shawn Pye"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101352512"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your sort_students_avg_insertion function after this line


# Do NOT include a main script in your submission
def sort_students_avg_insertion(students, order):
    if not students:
        return "Empty list."
    
    if not all("AvgGrade" in student for student in students):
        return "List not sorted. AvgGrade key not present."
    
    n = len(students)
    
    for i in range(1, n):
        key = students[i]
        j = i - 1
        
        if order == "A":
            while j >= 0 and students[j]["AvgGrade"] > key["AvgGrade"]:
                students[j + 1] = students[j]
                j -= 1
        elif order == "D":
            while j >= 0 and students[j]["AvgGrade"] < key["AvgGrade"]:
                students[j + 1] = students[j]
                j -= 1
        else:
            return "Invalid order. Use 'A' for ascending or 'D' for descending."
        
        students[j + 1] = key
    
    return "List sorted."