# Shantel Williams
# 12/15/2023
# Medium: Sales above Average

# For sales analysts, it’s often useful to identify which salespeople or products are performing above average. 
# Given a dictionary of product sales, create a function that identifies products whose sales are above the average sales for all products.

# product_sales = {
#     "Laptop": 1200,
#     "Smartphone": 700,
#     "Tablet": 500,
#     "Headphones": 300,
#     "Smartwatch": 400,
# }

# https://d-i-motion.com/topics/python-challenge-week-8/

def above_avg_sales(sale_dict):
    above = lambda key : sale_dict[key] > sum(sale_dict.values()) // len(sale_dict)
    return list(filter(above,sale_dict))

def main():
    product_sales = {
    "Laptop": 1200,
    "Smartphone": 700,
    "Tablet": 500,
    "Headphones": 300,
    "Smartwatch": 400,
}
    print(above_avg_sales(product_sales))
main()