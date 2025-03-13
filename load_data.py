# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "Houssem Ferchichi"

# Update "" with your team (e.g. T102)
__team__ = ""

#==========================================#
# Place your student_school_list function after this line
def student_school_list(file_name: str, school_name: str) -> list[dict[str, str]]:
    file = open(file_name,"r")
    filterkey = "School"
    filterstr = str(school_name)
    for line in file:
        keys = line.strip().split(",")
        break
    data=[]
    for line in file:
        header = {key : list for key in keys}
        values = line.strip().split(",")
        if values[keys.index(filterkey)]==filterstr:
            for i in range(len(values)):
                if i != keys.index(filterkey):
                    try:header[keys[i]]=int(values[i])
                    except:
                        try:header[keys[i]]=float(values[i])
                        except:header[keys[i]]=values[i]
            header.pop(filterkey)
            data.append(header)
    file.close()
    return data

#==========================================#
# Place your student_health_list function after this line
def student_health_list(file_name: str, health_status: int) -> list[dict[str, str]]:
    file = open(file_name,"r")
    filterkey = "Health"
    filterstr = str(health_status)
    for line in file:
        keys = line.strip().split(",")
        break
    data=[]
    for line in file:
        header = {key : list for key in keys}
        values = line.strip().split(",")
        if values[keys.index(filterkey)]==filterstr:
            for i in range(len(values)):
                if i != keys.index(filterkey):
                    try:header[keys[i]]=int(values[i])
                    except:
                        try:header[keys[i]]=float(values[i])
                        except:header[keys[i]]=values[i]
            header.pop(filterkey)
            data.append(header)
    file.close()
    return data
#==========================================#
# Place your student_age_list function after this line
def student_age_list(file_name: str, age: int) -> list[dict[str, str]]:
    file = open(file_name,"r")
    filterkey = "Age"
    filterstr = str(age)
    for line in file:
        keys = line.strip().split(",")
        break
    data=[]
    for line in file:
        header = {key : list for key in keys}
        values = line.strip().split(",")
        if values[keys.index(filterkey)]==filterstr:
            for i in range(len(values)):
                if i != keys.index(filterkey):
                    try:header[keys[i]]=int(values[i])
                    except:
                        try:header[keys[i]]=float(values[i])
                        except:header[keys[i]]=values[i]
            header.pop(filterkey)
            data.append(header)
    file.close()
    return data
#==========================================#
# Place your student_failures_list function after this line
def student_failures_list(file_name: str, failures: int) -> list[dict[str, str]]:
    file = open(file_name,"r")
    filterkey = "Failures"
    filterstr = str(failures)
    for line in file:
        keys = line.strip().split(",")
        break
    data=[]
    for line in file:
        header = {key : list for key in keys}
        values = line.strip().split(",")
        if values[keys.index(filterkey)]==filterstr:
            for i in range(len(values)):
                if i != keys.index(filterkey):
                    try:header[keys[i]]=int(values[i])
                    except:
                        try:header[keys[i]]=float(values[i])
                        except:header[keys[i]]=values[i]
            header.pop(filterkey)
            data.append(header)
    file.close()
    return data
#==========================================#
# Place your load_data function after this line
def load_data(file_name: str, dictfilter) -> list[dict[str, str]]:
    file = open(file_name,"r")
    if len(dictfilter) !=1 :
        print("Invalid Value")
        return []
    filter_key, filter_str = list(dictfilter.items())[0]
    if (filter_key not in ['School' , 'Age', 'Health', 'Failures','All']):
        print("Invalid Value")
        return []
    for line in file:
        keys = line.strip().split(",")
        break
    data=[]
    for line in file:
        header = {key : list for key in keys}
        values = line.strip().split(",")
        if values[keys.index(filter_key)]==str(filter_str) or filter_str == "All":
            for i in range(len(values)):
                if i != keys.index(filter_key):
                    try:header[keys[i]]=int(values[i])
                    except:
                        try:header[keys[i]]=float(values[i])
                        except:header[keys[i]]=values[i]
            header.pop(filter_key)
            data.append(header)
    file.close()
    return data
#==========================================#
# Place your add_average function after this line
def add_average(data: list[dict[str, str]]) -> list[dict[str, str]]:
    """Calculate each student's average grade and include it in the dictionary from a given dataset."""
    for row in data:
        try:
            row["AvgGrade"] = round((int(row["WinterGrade"]) + int(row["FallGrade"])) / 2, 2)
        except (ValueError, KeyError):
            row["AvgGrade"] = "N/A"
    return data

