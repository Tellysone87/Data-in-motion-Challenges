# 10/19/2023
# Shantel Williams

# Write a Python function that accepts a string and returns all email addresses found in the string. 
# Use regular expressions in your solution.

# input_string = ‘My email addresses are test1@example.com and test2@example.net’
import re

def find_address(a_string): # solution function that takes in a string
    pattern = '[\w\.-]+@[\w\.-]+'
    return re.findall(pattern, a_string)


def main():
    # test case

    input_string = 'My email addresses are test1@example.com and test2@example.net' 
    test = find_address(input_string)
    print(test)

main()