# Shantel Williams
# 12/20/2023

# Hard: Employee Performance
# Performance metrics are a common dataset in the corporate world, where each metric might have several sub-scores contributing to a final score.

# Given a list of employee performances, where each employee has multiple score categories, find the total score for each employee and create a function that identifies the employees whose score is in the top 10% of the group.

# employee_scores = [
#     {"name": "Alice", "scores": [85, 90, 88, 70, 80]},
#     {"name": "Bob", "scores": [80, 85, 85, 78, 90]},
#     {"name": "Charlie", "scores": [90, 92, 80, 85, 85]},
#     {"name": "David", "scores": [70, 75, 78, 80, 85]},
#     {"name": "Eva", "scores": [95, 88, 90, 80, 85]},
#     {"name": "Frank", "scores": [65, 60, 70, 75, 80]},
# ]

import numpy as np

def top_ten(emp_list):
    # write formula to grab top 10 percent
    sums = sorted([sum(employ["scores"]) for employ in emp_list])

    top_ten_percent = np.percentile(sums,90)
    print(top_ten_percent)
    print(sums)

    #filter data
    above = lambda emp : sum(emp["scores"]) > top_ten_percent
    new_list = list(filter(above,emp_list))

    # sort to show names
    names = lambda employees : employees["name"]
    return list(map(names, new_list))


def main():
    employee_scores = [
    {"name": "Alice", "scores": [85, 90, 88, 70, 80]},
    {"name": "Bob", "scores": [80, 85, 85, 78, 90]},
    {"name": "Charlie", "scores": [90, 92, 80, 85, 85]},
    {"name": "David", "scores": [70, 75, 78, 80, 85]},
    {"name": "Eva", "scores": [95, 88, 90, 80, 85]},
    {"name": "Frank", "scores": [65, 60, 70, 75, 80]},
    ]   

    print(top_ten(employee_scores))

main()