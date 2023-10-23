# 10/24/2023
# Shantel Williams

# Background:
# Often, data analysts need to extract specific fields from a list of dictionaries for reporting purposes.

# Problem Statement:
# Given a list of product details, use create a function to extract all product names.

# products = [
#     {"id": 1, "name": "Laptop", "price": 1000},
#     {"id": 2, "name": "Keyboard", "price": 25},
#     {"id": 3, "name": "Mouse", "price": 20},
# ]

def extract(list):
    names = [item["name"] for item in list]

    for name in names:
        print(name)
   
def main():

    products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Keyboard", "price": 25},
    {"id": 3, "name": "Mouse", "price": 20},
]
    extract(products)

    
main()

    