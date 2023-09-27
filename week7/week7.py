 # Date: 10/3/2023
 # Author: Shantel Williams

# Problem: Create a function that takes a list of dictionaries and returns the sum of people’s budgets.

# Examples:
# get_budgets([
# { "name": "John", "age": 21, "budget": 23000 },
# { "name": "Steve", "age": 32, "budget": 40000 },
# { "name": "Martin", "age": 16, "budget": 2700 }
# ]) ➞ 65700

# get_budgets([
# { "name": "John", "age": 21, "budget": 29000 },
# { "name": "Steve", "age": 32, "budget": 32000 },
# { "name": "Martin", "age": 16, "budget": 1600 }
# ]) ➞ 62600
def get_budgets(alist):
    our_sum = 0

    for each_dict in alist:
        our_sum += each_dict.get("budget")

    return our_sum

def main():

    tests = [
    get_budgets([
    { "name": "John", "age": 21, "budget": 23000 },
    { "name": "Steve", "age": 32, "budget": 40000 },
    { "name": "Martin", "age": 16, "budget": 2700 }
    ]),

    get_budgets([
    { "name": "John", "age": 21, "budget": 29000 },
    { "name": "Steve", "age": 32, "budget": 32000 },
    { "name": "Martin", "age": 16, "budget": 1600 }
    ])]

    for t in tests:
        print(t)

main()