 # Date: 10/9/2023
 # Author: Shantel Williams

import math

# Problem 1: Create a function that takes two arguments: the original price and the discount percentage as integers and returns the final price after the discount.

# TestCases:
# function{100,10} --> $90.00
# function{50,15} --> $42.50

def total_price(num1,num2):
    percentage = float(num2 / 100)

    total_discount = float(percentage * num1)

    return f" ${format(num1 - total_discount,'.2f')}"



# Problem 2: Create a function that takes the age in years and returns the age in days.
def convert_years_to_days(years):
    return f"Your are {years} years old, but {years * 365} days old."


# Problem 3: Create a function that takes an angle in radians 
# and returns the corresponding angle in degrees rounded to one decimal place.
def angle_in_radians(angle_in_radians):
    return f"{angle_in_radians} angle in radians converted to degrees is : {round(math.degrees(angle_in_radians),1)}"


def main():
    test = [
        # total_price(100,10),
        # total_price(50,15)
        # convert_years_to_days(2),
        # angle_in_radians(2)
    ]

    for t in test:
        print(t)

main()