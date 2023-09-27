 # Date: 9/26/2023
 # Author: Shantel Williams

# Problem: Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

# Examples:
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]
# filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]
# filter_list([1, 2, "aasf", "1", "123", 123]) ➞ [1, 2, 123]
def filter_list(a_string):

    # Conditional Solution
    # int_list = []

    # for element in a_string:
    #     if isinstance(element,int):
    #         int_list.append(element)

    # return int_list

    return [element for element in a_string if isinstance(element,int)] # list comprehension



def main():
    tests = [
    filter_list([1, 2, "a", "b"]),
    filter_list([1, "a", "b", 0, 15]),
    filter_list([1, 2, "aasf", "1", "123", 123]) ]
    
    for t in tests:
        print(t)

main()