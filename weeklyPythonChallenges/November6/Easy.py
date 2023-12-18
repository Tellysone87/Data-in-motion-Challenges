# Shantel Williams
# 12/18/2023

# Problem Statement: You have a list of ratings (from 1 to 5) given by customers for a product. Write a function to calculate the average rating.

# ratings = ['5', '3', '4', '2', '5', '5', '1']

def average_rating(rate_list):
    new_list = [int(num) for num in rate_list]

    return sum(new_list) // len(new_list)
    

def main():
    ratings = ['5', '3', '4', '2', '5', '5', '1']
    print(average_rating(ratings))

main()




