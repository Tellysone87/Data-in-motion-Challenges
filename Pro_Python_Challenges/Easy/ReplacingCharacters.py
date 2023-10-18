# 10/18/2023
# Shantel Williams

# Write a Python function that accepts a string and replaces all digits in the string 
# with the “#” symbol. Use regular expressions in your solution.

# input_string = ‘1234 Main St’
import re

def replace_digits(some_string):
    return re.sub("[0-9]", "#" ,some_string)


def main():
    input_string = '1234 Main St'

    test = replace_digits(input_string)

    print(test)

main()