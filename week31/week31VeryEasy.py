# Date: 8/16/2023
# Author: Shantel Williams

# Very easy: In this challenge, a farmer is asking you to tell him how many legs can be counted among all his animals. 
#The farmer breeds three species:
# chickens = 2 legs
# cows = 4 legs
# pigs = 4 legs
# The farmer has counted his animals and he gives you a subtotal for each species. 
# You have to implement a function that returns the total number of legs of all the animals.

# Examples:
# animals(2, 3, 5) ➞ 36
# animals(1, 2, 3) ➞ 22
# animals(5, 2, 8) ➞ 50

# Notes:
# Don’t forget to return the result.
# The order of animals passed is animals(chickens, cows, pigs).
# Remember that the farmer wants to know the total number of legs and not the total number of animals.
def animals(chickens,cows,pigs):
    """ Afunction that returns the total number of legs of all the animals. """
    total_legs  = 0 # variable to store total legs
    animal_leg_count = {"chickens": 2,"cow": 4 ,"pig": 4} # dictionary to store leg counts for designated animal

    #count animal legs
    total_legs += chickens * animal_leg_count.get("chickens", 0) # chickens times the stored legs value
    total_legs += cows * animal_leg_count.get("cow", 0) # cows times the stored legs value
    total_legs += pigs * animal_leg_count.get("pig", 0) # pigs times the stored legs value

    return total_legs

def main():
    test = animals(2, 3, 5)
    test2 = animals(1, 2, 3)
    test3 = animals(5, 2, 8)
    print(test)
    print(test2)
    print(test3)

main()