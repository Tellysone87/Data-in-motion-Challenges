# Date: 9/1/2023
# Author: Shantel Williams

# Create a function that takes a list of numbers and a string 
# and return a list of numbers as per the following rules:

# “Asc” returns a sorted list in ascending order.
# “Des” returns a sorted list in descending order.
# “None” returns a list without any modification.

# Examples:
# asc_des_none([4, 3, 2, 1], “Asc” ) ➞ [1, 2, 3, 4]
# asc_des_none([7, 8, 11, 66], “Des”) ➞ [66, 11, 8, 7]
# asc_des_none([1, 2, 3, 4], “None”) ➞ [1, 2, 3, 4]

def asc_des_none(num_list, sort):
    """ function that takes a list of numbers and a string 
    and return a list of numbers based on provided rules"""
    if not num_list:
         return "No numbers were provided"

# “Asc” returns a sorted list in ascending order.
    if sort == "Asc":
        return sorted(num_list)

# “Des” returns a sorted list in descending order.
    if sort == "Des":
            return sorted(num_list,reverse = True)

# “None” returns a list without any modification.
    if sort == "None":
        return num_list

def main():
    test = asc_des_none([4, 3, 2, 1], "Asc") 
    test2 = asc_des_none([7, 8, 11, 66], "Des")
    test3 = asc_des_none([1, 2, 3, 4], "None")
    test4 = asc_des_none([], "None")
    print(test)
    print(test2)
    print(test3)
    print(test4)
main()