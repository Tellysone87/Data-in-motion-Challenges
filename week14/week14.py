 # Date: 9/22/2023
 # Author: Shantel Williams

# Problem: Create a function that takes in a string as an input. If the string starts with a vowel, return True. If not, return False.

# Examples:
# starts_with_vowel(‘hello’) -> False
# starts_with_vowel(‘another’) -> True

def starts_with_vowel(a_string):

    # conditional solution:
    # vowel = ["a","e","i","o","u"]

    # if a_string[0] in vowel:
    #     return True
    
    # return False

    return a_string[0] in ["a","e","i","o","u"] # One line solution

def main():
    tests = [
        starts_with_vowel('hello'),
        starts_with_vowel('another') 
    ]

    for t in tests:
        print(t)

main()