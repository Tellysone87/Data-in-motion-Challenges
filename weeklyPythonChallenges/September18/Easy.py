# 11/27/2023
# Shantel Williams

# Easy Challenge: Uppercase and Lowercase Count
# Problem Statement
# Write a function count_case(s) that takes a string s and returns a dictionary with the count of uppercase and lowercase letters.

# # Example usage:
# print(count_case("Hello World")) # Output: {'uppercase': 2, 'lowercase': 8}
def count_case(s):
    case = {}

    for letter in s:
        if letter.isupper():
            if 'uppercase' in case:
                case['uppercase'] = case.get('uppercase', 0 ) + 1
            else:
                case['uppercase'] = 1
        if letter.islower():
            if 'lowercase' in case:
                case['lowercase'] = case.get('lowercase', 0 ) + 1
            else:
                case['lowercase'] = 1

    return case
        


def main():
    print(count_case("Hello World"))

main()