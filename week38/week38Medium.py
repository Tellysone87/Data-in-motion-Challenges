# Date: 7/10/2023
# Author: Shantel Williams

# Instructions: 
# Consider the following list of dictionaries

# products = [{"product": "A", "price": 12.20}, {"product": "B", "price": 15.60}, {"product": "C", "price": 9.10}]

# Write a Python function to find the most expensive product.

def most_expensive_product(provided_dict):
    """ function to find the most expensive product of the provided dictionary """

    most_expensive = ""  # setting variable to empty string and will assign new values within my loop
    highest = 0  # set default price of zero for comparing.

    for products in provided_dict: #looping through each dictionary located within the list
        if products['price'] > highest: # check each price to see if its greater than the previous
            highest = products['price'] # if it is, set the new highest price to that product
            most_expensive = products['product'] # set the product as the most expensive
        
    return most_expensive # return the most expensive product

def main():
    products = [{"product": "A", "price": 12.20}, {"product": "B", "price": 15.60}, {"product": "C", "price": 9.10}]

    test = most_expensive_product(products) ## callihg function with list of dictionaries as argument
    print(f"The highest product in the provided list is {test}")

main()