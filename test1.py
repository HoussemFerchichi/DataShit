# ECOR 1042 Lab 4 - Individual submission for test1 function

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

def test_return_list():
    passed = 0
    failed = 0
    #__________________________________________________________________________________________________________________

    #                                    load_data() -> 9 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = load_data("student-test.csv",{'Failures':0})
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = load_data("student-test.csv",{'Age':15})
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'Health':3})
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'School':"MS"})
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'All':999})
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'WrongEntry':"MS"})
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                 student_school_list() -> 5 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = student_school_list("student-test.csv","MS")
        assert isinstance(result, list), f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_school_list("student-test.csv","GP")
        assert isinstance(result, list), f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_school_list("student-test.csv","NOTINLIST")
        assert isinstance(result, list), f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                   student_health_list() -> 5 Test Cases
    #__________________________________________________________________________________________________________________
    
    try:
        result = student_health_list("student-test.csv",1)
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_health_list("student-test.csv","0")
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_health_list("student-test.csv","WrongDataType")
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1

    #__________________________________________________________________________________________________________________

    #                                    student_age_list() -> 6 Test Cases
    #__________________________________________________________________________________________________________________

    try:
        result = student_age_list("student-test.csv",15)
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_age_list("student-test.csv",9999)
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_age_list("student-test.csv","WrongDataType")
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                   student_failures_list() -> 5 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = student_failures_list("student-test.csv",0)
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_failures_list("student-test.csv",9999)
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_failures_list("student-test.csv","0")
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1

    #__________________________________________________________________________________________________________________

    #                                         add_average() -> 3 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = add_average([])
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = add_average(student_failures_list("student-test.csv",0))
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = add_average(student_age_list("student-test.csv",9999))
        assert isinstance(result, list), f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                           Total -> 34 Test Cases
    #__________________________________________________________________________________________________________________

    # Returning the count of passed and failed tests

    return [passed, failed] 


# Do NOT include a main script in your submission