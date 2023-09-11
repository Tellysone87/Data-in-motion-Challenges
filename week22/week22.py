# Date: 9/11/2023
# Author: Shantel Williams

# Define a function contains_blue() that accepts any number of arguments. 
# It should return True if any of the arguments are “blue” (all lowercase). Otherwise, it should return False .

# For example:

# contains_blue(25, “blue”) #True
# contains_blue(“green”, False, 37, “purple”, “hello world”) #False
# contains_blue(“blue”) #True
# contains_blue(“a”, 99, “blah blah blah”, 1, True, False, “blue”) #True
# contains_blue(1,2,3) #False

def contains_blue(*input): # *input will take in any number of arguments as a tuple.
    """ return True if any of the arguments are “blue”. Otherwise return False. """
    
    for argu in input: # iterating through the tuple of arguments
        if argu == "blue": # if the argument is equal to "blue"
            return True # you know, return True
        
    return False # default return unless condtion is met

def main():

    tests = [
    contains_blue(25, "blue") ,
    contains_blue("green", False, 37, "purple", "hello world") ,
    contains_blue("blue") ,
    contains_blue("a", 99, "blah blah blah", 1, True, False, "blue") ,
    contains_blue(1,2,3)]

    for test in tests:
        print(test)

main()