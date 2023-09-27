 # Date: 9/27/2023
 # Author: Shantel Williams

# Problem: Create a function that takes a string as input and capitalizes the string.

# Examples:
# capitalize_string(‘hello’) -> “Hello”
# capitalize_string(‘Again’) -> “Again”

# capitalize() will help with the solution
def capitalize_string(a_string):
    return a_string.capitalize()

def main():

    tests = [
    capitalize_string('hello'), 
    capitalize_string('Again')]

    for t in tests:
        print(t)

main()