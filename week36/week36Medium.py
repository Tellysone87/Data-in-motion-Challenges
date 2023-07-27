# Date: 7/21/2023
# Author: Shantel Williams

# Medium: Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM.

# Examples
# format_date(“11/12/2019”) ➞ “20191211”
# format_date(“12/31/2019”) ➞ “20193112”
# format_date(“01/15/2019”) ➞ “20191501”

# Notes:
# Return value should be a string.
def convert_date(Date):

    new_date = Date.split("/") # splits the string at the "/" symbol. Resulting in a list of date strings. Ex. ['11', '12', '2019']
    reversed_Date = new_date[::-1] # I then reversed the list to get the desired yyyy, dd , mm format. Ex ['2019', '12', '11']

    return ''.join(reversed_Date) # used the join method to return a string combining each string index of the reversed list. Ex. 20191211

def main():
    test = convert_date("11/12/2019") #  ➞ “20191211”
    test2 = convert_date("12/31/2019")  # ➞ “20193112”
    test3 = convert_date("01/15/2019")  # ➞ “20191501”

    print(test)
    print(test2)
    print(test3)


main()