 # Date: 9/28/2023
 # Author: Shantel Williams

# Problem 1: Write two functions:
# to_int() : A function to convert a string to an integer.
# to_str() : A function to convert an integer to a string.
def to_int(a_string):
    return int(a_string)

def to_str(a_int):
    return str(a_int)

# Problem 2: Create a function that takes a number as its only argument and returns True if it’s less than or equal to zero, otherwise return False.
def check(some_int):
    return some_int <= 0

# Bonus (Optional)
# Create a function that takes two number strings and returns their sum as a string.
def string_sun(string1,string2):
    return str(int(string1) + int(string2))

def main():
    test = [ 
        # coding question 1 tests
            to_int("3"),
            to_str(6),
        
        # coding question 2 tests
            check(-1),
            check(3),

        # Bonus question 3 test
            string_sun("6","2")]

    for t in test:
        print(t)
        print(type(t))

main()