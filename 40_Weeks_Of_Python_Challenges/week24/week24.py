# Date: 9/7/2023
# Author: Shantel Williams

# Create a function, yell, which accepts a single string argument. 
# It should return(not print) an uppercased version of the string with an exclamation point added at the end. 

# For example:
# yell(“go away”) # “GO AWAY!”
# yell(“leave me alone”) # “LEAVE ME ALONE!”

def yell(some_string):
    """ returns an uppercased version of the string with an exclamation point added at the end. """
    return F"{some_string.upper()}!"

def main():

    test = [
    yell("go away"),
    yell("leave me alone")
    ]

    for tests in test:
        print(tests)

main()