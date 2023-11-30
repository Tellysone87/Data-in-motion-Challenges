# Shantel Williams
# 11/30/2023

# Write a function is_perfect_square(n) that takes a positive integer n and returns True if it’s a perfect square and False otherwise. 
# A perfect square is an integer that can be expressed as the square of another integer such as 25 (5×5) or 16 (4×4).

# # Example usage:
# print(is_perfect_square(16)) # Output: True
# print(is_perfect_square(17)) # Output: False

def is_perfect_square(n):
    i =0

    while i < n:
        if i * i == n:
            return True
        i = i + 1
        
    return False
    


def main():
    print(is_perfect_square(16)) # Output: True
    print(is_perfect_square(17)) # Output: False

main()