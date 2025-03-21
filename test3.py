# ECOR 1042 Lab 4 - Individual submission for test3 function

# import load_data module here

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""

#==========================================#
# Do not modify the code alreayd provided.


def test_return_correct_dict_inside_list() -> list[int]:
    from load_data import load_data, student_school_list, student_health_list, student_age_list, student_failures_list, add_average
    passed = 0
    failed = 0
    
    #__________________________________________________________________________________________________________________

    #                                    load_data() -> 6 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = load_data("student-test.csv",{'Failures':0})
        assert len(result[0]) == 8 and len(result[-1])==8 and "Failures" not in result[0] and "Failures" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = load_data("student-test.csv",{'Age':15})
        assert len(result[0]) == 8 and len(result[-1])==8 and "Age" not in result[0] and "Age" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'Health':3})
        assert len(result[0]) == 8 and len(result[-1])==8 and "Health" not in result[0] and "Health" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'School':"MS"})
        assert len(result[0]) == 8 and len(result[-1])==8 and "School" not in result[0] and "School" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'All':999})
        assert len(result[0]) == 9 and len(result[-1])==9, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = load_data("student-test.csv",{'Health':5})
        assert len(result[0]) == 8 and len(result[-1])==8 and "Health" not in result[0] and "Health" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                 student_school_list() -> 3 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = student_school_list("student-test.csv","MS")
        assert len(result[0]) == 8 and len(result[-1])==8 and "School" not in result[0] and "School" not in result[-1], f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_school_list("student-test.csv","GP")
        assert len(result[0]) == 8 and len(result[-1])==8 and "School" not in result[0] and "School" not in result[-1], f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = student_school_list("student-test.csv","MB")
        assert len(result[0]) == 8 and len(result[-1])==8 and "School" not in result[0] and "School" not in result[-1], f"student_school_list did not return a list, returned: {type(result)}"
        passed += 1
    except AssertionError:
        failed += 1
    
    #__________________________________________________________________________________________________________________

    #                                   student_health_list() -> 3 Test Cases
    #__________________________________________________________________________________________________________________
    
    try:
        result = student_health_list("student-test.csv",1)
        assert len(result[0]) == 8 and "Health" not in result[0] , f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_health_list("student-test.csv",4)
        assert len(result[0]) == 8 and len(result[1])==8 and len(result[-1])==8 and "Health" not in result[0] and "Health" not in result[1] and "Health" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_health_list("student-test.csv",3)
        assert len(result[0]) == 8 and len(result[-1])==8 and "Health" not in result[0] and "Health" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1

    #__________________________________________________________________________________________________________________

    #                                    student_age_list() -> 3 Test Cases
    #__________________________________________________________________________________________________________________

    try:
        result = student_age_list("student-test.csv",15)
        assert len(result[0]) == 8 and len(result[1])==8 and len(result[-1])==8 and "Age" not in result[0] and "Age" not in result[1] and "Age" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_age_list("student-test.csv",16)
        assert len(result[0]) == 8 and len(result[-1])==8 and "Age" not in result[0] and "Age" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_age_list("student-test.csv",18)
        assert len(result[0]) == 8 and len(result[-1])==8 and "Age" not in result[0] and "Age" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                   student_failures_list() -> 3 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = student_failures_list("student-test.csv",2)
        assert len(result[0]) == 8 and len(result[-1])==8 and "Failures" not in result[0] and "Failures" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_failures_list("student-test.csv",3)
        assert len(result[0]) == 8 and "Failures" not in result[0], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = student_failures_list("student-test.csv",0)
        assert len(result[0]) == 8 and len(result[-1])==8 and "Failures" not in result[0] and "Failures" not in result[-1], f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1

    #__________________________________________________________________________________________________________________

    #                                         add_average() -> 3 Test Cases
    #__________________________________________________________________________________________________________________
    try:
        result = add_average(student_failures_list("student-test.csv",0))
        assert len(result[0]) == 9 and len(result[-1])==9 and "AvgGrade" in result[0] and "AvgGrade" in result[-1] and list(result[0]).index("AvgGrade") == 8 and list(result[-1]).index("AvgGrade") == 8, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    
    try:
        result = add_average(student_age_list("student-test.csv",18))
        assert len(result[0]) == 9 and len(result[-1])==9 and "AvgGrade" in result[0] and "AvgGrade" in result[-1] and list(result[0]).index("AvgGrade") == 8 and list(result[-1]).index("AvgGrade") == 8, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    try:
        result = add_average(student_failures_list("student-test.csv",2))
        assert len(result[0]) == 9 and len(result[-1])==9 and "AvgGrade" in result[0] and "AvgGrade" in result[-1] and list(result[0]).index("AvgGrade") == 8 and list(result[-1]).index("AvgGrade") == 8, f"add_average failed test number: {abs(passed - failed) + 1}"
        passed += 1
    except AssertionError:
        failed += 1
    #__________________________________________________________________________________________________________________

    #                                           Total -> 21 Test Cases
    #__________________________________________________________________________________________________________________

    # Returning the count of passed and failed tests

    return [passed, failed] 
# Do NOT include a main script in your submission
