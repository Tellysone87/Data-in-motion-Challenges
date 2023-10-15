# Date: 8/28/2023
# Author: Shantel Williams

# Easy: Create a function that takes a list of non-negative integers and strings and return a new list without the strings.

# filter_list([1, 2, “a”, “b”]) ➞ [1, 2]
# filter_list([1, “a”, “b”, 0, 15]) ➞ [1, 0, 15]
# filter_list([1, 2, “aasf”, “1”, “123”, 123]) ➞ [1, 2, 123]

def filter_list(sting_list):
    New_list = []

    for item in sting_list:
        if type(item) != str:
            New_list.append(item)

    return New_list

def main():
    test =filter_list([1, 2, "a", "b"])
    test2 = filter_list([1, "a", "b", 0, 15]) 
    test3 = filter_list([1, 2, "aasf", "1", "123", 123])
    print(test)
    print(test2)
    print(test3)

main()