# Date: 7/17/2023
# Author: Shantel Williams

# Medium: Given a list of tuples representing student information like:

# students = [(“John”, 15, “Grade 10”), (“Emily”, 14, “Grade 9”), (“Sam”, 16, “Grade 11”)], 
                                                                                                                                                                                                                                                              
# write a Python function to filter out the students who are older than 15.

def filter_age(list_of_students):
    # function to filter out the students who are older than 15.

    # filter_student will grab each student from the provided list that has a age greater than 15. 
    filtered_students = [ student for student in list_of_students if student[1] > 15] # practicing list comprehension. 

    return filtered_students # return filtered list

def main():
    students = [("john", 15, "Grade 10"), ("Emily", 14, "Grade 9"), ("Sam", 16, "Grade 11")]
    print(filter_age(students))

main()
