# Hard Challenge: Nested Data Parsing
# You are given a list of dictionaries. Each dictionary contains information about a student. 
# A student dictionary has the following keys: 'name', 'subjects', and 'grades'. The 'subjects' key is associated with a list of subjects, 
# and the 'grades' key is associated with a list of grades. Both lists are of the same length.

# Your task is to use functional programming constructs to: 
# Filter the students who have an average grade above a certain threshold.
# Extract the name of the student and their highest grade.  
# Sort the resulting list by the highest grade in descending order.
# Define a function top_students(student_list, grade_threshold) that accomplishes the above tasks using Python’s filter(), map(), and sorted() functions. 
# You may also need to use built-in functions like sum() and len().

def top_students(student_list, grade_threshold):
    # Filter the students who have an average grade above a certain threshold

    # test = [student for student in student_list if sum(student['grades']) // len(student['grades']) > grade_threshold]
    avg_above_threshold = lambda student : sum(student['grades']) // len(student['grades']) > grade_threshold
    grades = list(filter(avg_above_threshold, student_list))

    # map - Extract the name of the student and their highest grade.
    student_name = lambda student: f"Student: {student['name']}  Max Grade: {max(student['grades'])}"
    student_record = list(map(student_name, grades))
    
    # Sort the resulting list by the highest grade in descending order.
    return  sorted(student_record, reverse=True)

def main():
    students = [
        {'name': 'Alice', 'subjects': ['Math', 'English'], 'grades': [85, 88]},
        {'name': 'Bob', 'subjects': ['Math', 'Biology'], 'grades': [90, 78]},
        {'name': 'Charlie', 'subjects': ['Biology', 'Physics'], 'grades': [82, 95]},
        {'name': 'David', 'subjects': ['English', 'History'], 'grades': [88, 90]}
    ]
    grade_threshold_sample = 85

    print(top_students(students,grade_threshold_sample))

main()