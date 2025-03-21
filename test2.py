# ECOR 1042 Lab 4 - Individual submission for test2 function

# import load_data module here

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""

#==========================================#
# Do not modify the code alreayd provided.
from load_data import load_data, student_school_list, student_health_list, student_age_list, student_failures_list, add_average

def test_return_list_correct_length() -> list[int]:
    passed = 0
    failed = 0
    
    #__________________________________________________________________________________________________________________

    #                                    load_data() -> 10 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = load_data("student-test.csv",{'Failures':0})
        assert len(result) == 11, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = load_data("student-test.csv",{'Age':15})
        assert len(result) == 3, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'Health':3})
        assert len(result) == 8, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'School':"MS"})
        assert len(result) == 4, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'All':999})
        assert len(result) == 15, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = load_data("student-test.csv",{'School':"GP"})
        assert len(result) == 3, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    #__________________________________________________________________________________________________________________

    #                                 student_school_list() -> 5 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = student_school_list("student-test.csv","MS")
        assert len(result) == 4, f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_school_list("student-test.csv","GP")
        assert len(result) == 3, f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_school_list("student-test.csv",9999)
        assert len(result) == 0, f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    #__________________________________________________________________________________________________________________

    #                                   student_health_list() -> 5 Test Cases
    #__________________________________________________________________________________________________________________
    
    try:
        result = student_health_list("student-test.csv",1)
        assert len(result) == 1, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_health_list("student-test.csv",0)
        assert len(result) == 0, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_health_list("student-test.csv",3)
        assert len(result) == 8, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1

    #__________________________________________________________________________________________________________________

    #                                    student_age_list() -> 6 Test Cases
    #__________________________________________________________________________________________________________________

    try:
        result = student_age_list("student-test.csv",15)
        assert len(result) == 3, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_age_list("student-test.csv",9999)
        assert len(result) == 0, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_age_list("student-test.csv",16)
        assert len(result) == 2, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                   student_failures_list() -> 5 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = student_failures_list("student-test.csv",2)
        assert len(result) == 2, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_failures_list("student-test.csv",9999)
        assert len(result) == 0, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_failures_list("student-test.csv",0)
        assert len(result) == 11, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1

    #__________________________________________________________________________________________________________________

    #                                         add_average() -> 4 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = add_average([])
        assert len(result) == 0, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = add_average(student_failures_list("student-test.csv",0))
        assert len(result) == 11, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = add_average(student_age_list("student-test.csv",18))
        assert len(result) == 4, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                           Total -> 35 Test Cases
    #__________________________________________________________________________________________________________________

    # Returning the count of passed and failed tests

    return [passed, failed]

# Do NOT include a main script in your submission
