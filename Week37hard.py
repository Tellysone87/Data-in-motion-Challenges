# Date: 7/17/2023
# Author: Shantel Williams
# Hard: Let’s assume you have a list of tuples stored in the variable transactions, each representing a transaction in an e-commerce store 
# where the first element is the transaction ID, the second element is the product ID, and the third element is the price.

# Write a Python function to find the product with the highest total sales.
def highest_total_sales(list_of_products):
    """ A function to find the product with the highest total sales. """

    # Per instructions, each product tuple layout is as follows: (transaction ID, Product ID, Price)
    # create a library to store the total sales per product ID. --- Key: Product ID  Value: Total sales
    Product_sales = {}

    for transaction in list_of_products: # loop through transactions
        if transaction[1] not in Product_sales: # if a key for the product key does not exist, add the key and the price for that transaction.
            Product_sales[transaction[1]] = transaction[2]
        elif transaction[1] in Product_sales: # if the key does exist, add that new purchase price to the existing one.
            Product_sales[transaction[1]] = Product_sales.get(transaction[1],0) + transaction[2]

    print(Product_sales)

    return max(Product_sales, key=Product_sales.get) # used get() and max() to display the product ID with the highest value. 

def main():
    # provided list of tuples
    transactions = [(1, 101, 15.0),(2, 102, 20.0),(3, 101, 15.0),(4, 103, 10.0),(5, 102, 20.0),(6, 101, 15.0),(7, 103, 10.0),
(8, 102, 20.0),(9, 103, 10.0),]
    
    highest_sale = highest_total_sales(transactions) # storing my function call with the provided list in a variable
    print(highest_sale) # printing the results

main()