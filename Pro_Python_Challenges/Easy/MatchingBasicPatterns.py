# 10/15/2023
# Shantel Williams

# Write a Python function that accepts a string and checks if the string starts with “Hello”. If it does, return True. 
# If not, return False. Use regular expressions in your solution.

# test_string = ‘Hello World’

import re

def check(some_string):
    
    hello = re.search("^Hello", some_string)
    if hello:
        return True
    else:
        return False


def main():
    test = [
        check("Hello there!"),
        check("This should be false")
    ]

    for t in test:
        print(t)


main()