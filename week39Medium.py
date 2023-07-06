# Author: Shantel Williams
# Date: 7/6/2023

# summary :
# Write a Python function that takes two lists as input 
# and returns a new list containing the common elements between the two lists.

def common(list1,list2):
    """ function returns a new list containing the common elements between the two lists."""

    # first check fo empty list or missing list
    if not list1 or not list2:
        return "No list to compare"

    common_list = [] # new list to store common values between list1 and list2

    set1 = set(list1) # created sets to remove any duplictes that may be present
    set2 = set(list2)

    for item in set1: # if current item in the set is in set2, add it to the common_list
        if item in set2:
            common_list.append(item)

    return common_list # returns the items that match


def main():
    #simple test
    l1 = [3,4,5] # list1
    l2 = [4,5,6] # list2

    # duplicate test
    l3 = [3,3,4,4,5,5,6,7]
    l4 = [3,4,6,8]

    # pass empty list
    l5 = []

    print(f"Simple test -- {common(l1,l2)}") # print the returned value of the common function
    print(f"duplicate test -- {common(l3,l4)}")
    print(f"empty list test -- {common(l3,l5)}")

main()