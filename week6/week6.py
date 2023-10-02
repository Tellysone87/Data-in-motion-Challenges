 # Date: 10/4/2023
 # Author: Shantel Williams

# Create a function that returns True when num1 is equal to num2; otherwise return False

# Examples:
# is_same_num(4, 8) ➞ False
# is_same_num(2, 2) ➞ True
# is_same_num(2, “2”) ➞ False
def is_same_num(num1,num2):
    return num1 == num2




def main():
    test = [
        is_same_num(4, 8), 
        is_same_num(2, 2),
        is_same_num(2, "2")
    ]

    for t in test:
        print(t)

main()