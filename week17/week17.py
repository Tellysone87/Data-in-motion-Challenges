 # Date: 9/18/2023
 # Author: Shantel Williams

# ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits. 
# Your task is to create a function that takes a string and returns True if the PIN is valid and False if it’s not.

# Examples:
# is_valid_PIN(“1234”) ➞ True
# is_valid_PIN(“12345”) ➞ False
# is_valid_PIN(“a234”) ➞ False
# is_valid_PIN(“”) ➞ False
def is_valid_PIN(A_string):

    if not A_string: # if string is empty
        return False
    
    if len(A_string) != 4 and len(A_string) != 6: # must be 4 or 6 in length
        return False
    
    if A_string.isnumeric() == False: # checks if the string is a number
        return False
    
    return True # returns true if not if the conditions are caught

def main():
    tests = [
    is_valid_PIN("1234"), 
    is_valid_PIN("12345"),
    is_valid_PIN("a234"),
    is_valid_PIN("")]

    for test in tests:
        print(test)


main()