# Date: 9/1$/2023
# Author: Shantel Williams

# Problem: Create a function that takes a number num and returns its length.

# Examples:
# number_length(10) ➞ 2
# number_length(5000) ➞ 4
# number_length(0) ➞ 1
def number_length(num):
    return len(str(num))

def main():
    tests = [
    number_length(10),
    number_length(5000),
    number_length(0)]

    for test in tests:
        print(test)

main()