# ECOR 1042 Lab 5 - Individual submission for sort_students_failures_bubble function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nicole Chen"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101343450"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-28"

#==========================================#
# Place your sort_students_failures_bubble function after this line


# Do NOT include a main script in your submission
def sort_students_failures_bubble(student_list, sort_order):
    # Check if the list is empty
    if not student_list:
        return "Empty list."
    
    # Check if the 'Failures' key exists in the dictionaries
    if 'Failures' not in student_list[0]:
        return "List not sorted. Failures key not present."
    
    # Bubble sort implementation for sorting the list based on 'Failures' key
    n = len(student_list)
    
    # Perform bubble sort
    for i in range(n):
        for j in range(0, n-i-1):
            # Compare based on the sort order
            if sort_order == "A":  # Ascending order
                if student_list[j]['Failures'] > student_list[j+1]['Failures']:
                    student_list[j], student_list[j+1] = student_list[j+1], student_list[j]
            elif sort_order == "D":  # Descending order
                if student_list[j]['Failures'] < student_list[j+1]['Failures']:
                    student_list[j], student_list[j+1] = student_list[j+1], student_list[j]
            else:
                return "Invalid sort order. Use 'A' for ascending or 'D' for descending."
    
    return "List sorted."
