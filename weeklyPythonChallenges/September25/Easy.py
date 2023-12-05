# Shantel Williams
# 12/5/2023

# Easy Challenge: Duplicate Detector
# Write a function named has_duplicates(lst) that accepts a list and returns True if the list contains any duplicates, otherwise False.

# list1 = [1, 2, 3, 4, 5]
# list2 = [5, 4, 3, 2, 5]
# list3 = ['a', 'b', 'c', 'a']

def has_duplicates(alist):
    remove_dup = set() # create set to remove duplicates

    for item in alist: # add each list item to set
        remove_dup.add(item)

    if len(remove_dup) != len(alist): # check set length against list length
        return True
    else:
        return False

def main():
    print(has_duplicates([1, 2, 3, 4, 5]))
    print(has_duplicates([5, 4, 3, 2, 5]))
    print(has_duplicates(['a', 'b', 'c', 'a']))


main()