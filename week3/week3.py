 # Date: 10/9/2023
 # Author: Shantel Williams

# Problem 2: Create a function that takes the age in years and returns the age in days.
# Problem 3: Create a function that takes an angle in radians and returns the corresponding angle in degrees rounded to one decimal place.
# Bonus (Optional)
# Create a function, get_days, that takes two dates and returns the number of days between the first and second date


# Problem 1: Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

# TestCases:
# function{100,10} --> $90.00
# function{50,15} --> $42.50
def total_price(num1,num2):
    percentage = float(num2 / 100)

    total_discount = float(percentage * num1)
    
    return f" ${format(num1 - total_discount,'.2f')}"



def main():
    test = [
        total_price(100,10),
        total_price(50,15)
    ]

    for t in test:
        print(t)

main()