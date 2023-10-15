# Date: 9/13/2023
# Author: Shantel Williams

# Write a function called number_compare. This function takes in two parameters (both numbers). 
# If the first is greater than the second, this function returns “First is greater” 
# If the second number is greater than the first, the function returns “Second is greater” 
# Otherwise the function returns “Numbers are equal”

def number_compare(num1,num2):

    # If the first is greater than the second, this function returns “First is greater”
    if num1 > num2: 
        return "First is greater"

    # If the second number is greater than the first, the function returns “Second is greater” 
    elif num2 > num1:
        return "Second is greater"

    # Otherwise the function returns “Numbers are equal”
    else:
        return "Numbers are equal"


def main():
    test = [
        
        number_compare(1,2),
        number_compare(8,8),
        number_compare(6,3)
    ]

    for t in test:
        print(t)


main()