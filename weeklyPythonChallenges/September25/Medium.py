# Shantel Williams
# 12/6/2023

# Medium Challenge: Filtered Squares
# Write a function named filtered_squares(limit, divisor) that:

# Generates a list of squares of numbers from 1 up to (and including) the provided limit.
# Filters the list to only include numbers that are divisible by the provided divisor.
# limit1, divisor1 = 10, 4
# limit2, divisor2 = 20, 5

def filtered_squares(limit, divisor):
    squares = []

    for i in range(1,limit +1):
        squares.append(i * i)

    print(squares)
    final_list = [num for num in squares if num%divisor == 0]

    return final_list

def main():
    print(filtered_squares(10, 4))
    print(filtered_squares(20, 5))

main()