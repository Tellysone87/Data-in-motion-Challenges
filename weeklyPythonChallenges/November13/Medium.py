# Shantel Williams
# 12/29/2023

# https://d-i-motion.com/topics/python-challenge-week-10/

# Problem Statement: You have a dataset containing customer IDs and their purchase amounts in various categories. 
# Segment the customers into three categories: ‘High’, ‘Medium’, and ‘Low’ based on their total purchase amounts.

# Segmentation Logic:
# High: Total purchases > 1500
# Medium: Total purchases between 500 and 1500
# Low: Total purchases < 500

# Expected Task: Write a function to categorize each customer based on their total purchase amount 
# and return a dictionary with customer IDs and their respective segments.

# purchases = [
#     {'customer_id': 1, 'electronics': 200, 'furniture': 700, 'stationery': 100},
#     {'customer_id': 2, 'electronics': 300, 'furniture': 300, 'stationery': 300},
#     {'customer_id': 3, 'electronics': 100, 'furniture': 100, 'stationery': 50},
#     {'customer_id': 4, 'electronics': 800, 'furniture': 1000, 'stationery': 200}
# ]
def segment_customers(purchase_list):
    category = {} # Empty dictionary to hold segments

    # Function to collect each customer total purchase amounts
    total = lambda customer: customer['electronics'] + customer['furniture'] + customer['stationery']

    for cust in purchase_list: # loop to grab total and check which segment the customer belong in.

        print(total(cust)) # print statmen to check total amounts

        if total(cust) > 1500:
            category[cust['customer_id']] = "High"  # high condition
        elif total(cust) <= 1500 and total(cust) >= 500:
            category[cust['customer_id']] = "Medium" # medium condition
        elif total(cust) < 500:
            category[cust['customer_id']] = "low" # low condition

    return category # return Dictionary

def main():
    purchases = [
        {'customer_id': 1, 'electronics': 200, 'furniture': 700, 'stationery': 100},
        {'customer_id': 2, 'electronics': 300, 'furniture': 300, 'stationery': 300},
        {'customer_id': 3, 'electronics': 100, 'furniture': 100, 'stationery': 50},
        {'customer_id': 4, 'electronics': 800, 'furniture': 1000, 'stationery': 200},
        {'customer_id': 5, 'electronics': 200, 'furniture': 200, 'stationery': 100},
        {'customer_id': 6, 'electronics': 500, 'furniture': 500, 'stationery': 500}
    ]

    print(segment_customers(purchases))

main()