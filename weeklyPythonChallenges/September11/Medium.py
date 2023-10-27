# 10/31/2023
# Shantel Williams

# Medium: Student Grade Manager
# Write a function add_grade(student_grades, student, grade) that takes a dictionary student_grades, 
# a string student, and an integer grade. The function should add the grade to the student’s list 
# of grades in the dictionary and return the updated dictionary.

# student_grades = {
# "Alice": [90, 85],
# "Bob": [80, 85],
# "Charlie": [70, 75],
# }
def add_grade(student_grades, student, grade):

    if student not in student_grades:
        return "student not found."
    
    student_grades[student].append(grade)

    return student_grades

def main():
    student_grades = {
    "Alice": [90, 85],
    "Bob": [80, 85],
    "Charlie": [70, 75],
    }

    print(add_grade(student_grades,"alice", 78))
    print(add_grade(student_grades,"Alice", 78))

main()
