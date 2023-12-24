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
    pass

def main():
    purchases = [
        {'customer_id': 1, 'electronics': 200, 'furniture': 700, 'stationery': 100},
        {'customer_id': 2, 'electronics': 300, 'furniture': 300, 'stationery': 300},
        {'customer_id': 3, 'electronics': 100, 'furniture': 100, 'stationery': 50},
        {'customer_id': 4, 'electronics': 800, 'furniture': 1000, 'stationery': 200}
    ]

    print(segment_customers(purchases))

main()