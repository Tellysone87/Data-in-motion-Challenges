# 10/26/2023
# Shantel Williams

# Hard: Nested Data Extraction & Summation
# Background:
# Data analysts sometimes work with nested data structures. The ability to extract and compute with such structures is crucial.

# Problem Statement:
# Given a nested list of transaction data where each list consists of transaction details, create a function that extract all the sales and compute their total sum.

# transactions = [
#     [{"id": 1, "sale": 100}, {"id": 2, "sale": 150}, {"id": 3, "sale": 200}],
#     [{"id": 4, "sale": 50}, {"id": 5, "sale": 300}],
#     [{"id": 6, "sale": 25}],
# ]
def extract_sales(some_list):
    sum = 0 
    for list in some_list:
        for transaction in list:
            sum += transaction["sale"]

    return sum

def main():
    transactions = [

    [{"id": 1, "sale": 100}, {"id": 2, "sale": 150}, {"id": 3, "sale": 200}],
    [{"id": 4, "sale": 50}, {"id": 5, "sale": 300}],
    [{"id": 6, "sale": 25}]

    ]
    print(extract_sales(transactions))


main()