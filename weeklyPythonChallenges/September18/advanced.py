# Shantel Williams
# 12/4/2023

# Advanced Challenge: Decimal to Binary Converter
# Write a function decimal_to_binary(n) that takes a non-negative integer n and returns its binary representation as a string.

# # Example usage:
# print(decimal_to_binary(10)) # Output: '1010'
def decimal_to_binary(n):
    num = []

    while n > 0:   # 10/2 = 5 r"0", 5/2 = 2 r"1", 2/2 =  1 r"0", 1/2 = 0 r"1"
        num.append(str(n%2)) # append remainder to list
        sub = n//2 # divide number for new value
        n = sub 

    rev_num = reversed(num) # reversed because the binary number would be from the bottom up

    return "".join(rev_num) # return string binary

def main():
    print(decimal_to_binary(10))
    print(decimal_to_binary(8))
    print(decimal_to_binary(13))
    print(decimal_to_binary(75))

main()