# Date: 9/6/2023
# Author: Shantel Williams

# Write a function named only_ints that takes two parameters. 
# Your function should return True if both parameters are integers, and False otherwise.

# For example, calling only_ints(1, 2) should return True, while calling only_ints(“a”, 1) should return False.
def only_ints(entry1,entry2):
   """ Function returns True if both parameters are integers, and False otherwise."""

   if type(entry1) == int and type(entry2) == int: # if both entries are int return True
       return True
   else:           # otherwise return False
       return False

def main():
    test = only_ints(1, 2)
    test2 = only_ints("a", 1)
    print(test)
    print(test2)

main()