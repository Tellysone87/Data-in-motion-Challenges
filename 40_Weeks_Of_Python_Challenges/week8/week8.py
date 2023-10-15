 # Date: 10/2/2023
 # Author: Shantel Williams

# Problem: Create a function that takes in a string as an input. If the string starts with a vowel, return True. If not, return False.

# Examples:
# starts_with_vowel(‘hello’) -> False
# starts_with_vowel(‘another’) -> True
def starts_with_vowel(a_string):
    
    vowels = ["a","e","i","o","u"]
    return a_string[0] in vowels

def main():

    test = [
    starts_with_vowel('hello'),
    starts_with_vowel('another') ]

    for t in test:
        print(t)

main()