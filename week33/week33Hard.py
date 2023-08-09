# Date: 8/9/2023
# Author: Shantel Williams
# Hard:
# Create a function to perform basic arithmetic operations that includes addition, subtraction, multiplication
# and division on a string number (e.g. “12 + 24” or “23 – 21” or “12 // 12” or “12 * 21”).
                                 
# Here, we have 1 followed by a space, operator followed by another space and 2. 
# For the challenge, we are going to have only two numbers between 1 valid operator. 
# The return value should be a number.
# eval() is not allowed. In case of division, whenever the second number equals “0” return -1.

# For example:
# “15 // 0” ➞ -1

# Examples:
# arithmetic_operation(“12 + 12”) ➞ 24
# arithmetic_operation(“12 – 12”) ➞ 0
# arithmetic_operation(“12 * 12”) ➞ 144
# arithmetic_operation(“12 // 0”) ➞ -1

# Notes:
# All the inputs are only integers.
# The operators are * – + and //.
# Hint: Think about the single space that appears before and after the arithmetic operator.

def arithmetic_operation(string_number):
    """ Function to perform basic arithmetic operations that includes addition, subtraction, multiplication and division on a string number """
    answer = 0 # set initial answer to zero

    seperated_string = string_number.split(" ")# split provided string into a list. Example: “12 + 12” --> ['12', '+', '12']
    
    # conditions to determine operator
    if seperated_string[1] == "+":
        answer = int(seperated_string[0]) + int(seperated_string[2])

    if seperated_string[1] == "-":
        answer = int(seperated_string[0]) - int(seperated_string[2])

    if seperated_string[1] == "*":
        answer = int(seperated_string[0]) * int(seperated_string[2])

    if seperated_string[1] == "//":
        if int(seperated_string[2]) == 0:
            answer = -1
        else:
            answer = int(seperated_string[0]) / int(seperated_string[2])
   
    return answer

def main():
    test1 = arithmetic_operation("12 + 12")
    test2 = arithmetic_operation("12 - 12")
    test3 = arithmetic_operation("12 * 12")
    test4 = arithmetic_operation("12 // 0")
    print(test1)
    print(test2)
    print(test3)
    print(test4)

main()