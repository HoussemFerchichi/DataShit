# ECOR 1042 Lab 3 - Individual submission for student_school_list function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
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
# Do NOT include a main script in your submission