# Date: 7/19/2023
# Author: Shantel Williams

# In Python, OOP allows us to encapsulate related properties and behaviors into individual objects. This challenge will involve creating a simple class and methods.
# The problem is to create a Circle class that represents a circle. The circle will be initialized with a radius. The class should have the following methods:

# get_radius(): This method should return the radius of the circle.
# set_radius(new_radius): This method should set a new radius for the circle.
# calculate_area(): This method should calculate and return the area of the circle using the formula πr^2. You can use 3.14 as the approximation for π.
# calculate_circumference(): This method should calculate and return the circumference of the circle using the formula 2πr.
# To test your implementation, create an instance of the circle with a radius of 5, update the radius to 10, and then calculate the area and circumference.

import math

#create a Circle class
class Circle:
    def __init__(self, radius):
        self._radius = radius # _raduis allows us to keep the variable protected and prevent direct access from outside the class. 

    def get_raduis(self):
        """ This method should return the radius of the circle."""
        return self._radius

    def set_radius(self, new_radius):
        """ This method should set a new radius for the circle."""
        self._radius = new_radius

    def calculate_area(self):
        """ This method should calculate and return the area of the circle using the formula πr^2. You can use 3.14 as the approximation for π."""
        return math.pow(self._radius, 2) * 3.14  # area = (π * Radius * Radius )

    def calculate_circumference(self):
        """ This method should calculate and return the circumference of the circle using the formula 2πr."""
        return 2 * self._radius * 3.14


def main():
    test = Circle(5) # create instance of circle
    print(test.get_raduis()) # print the radius

    test.set_radius(3) # set the radius to 10
    print(test.get_raduis()) # print the new radius

    # calculate the area and circumference.
    print(f"The circles area is : {round(test.calculate_area(), 2)}") # Note: I did round the results to remove the extra zeros
    print(f"The circles circumference is: {round(test.calculate_circumference(), 2)}")

    try: # testing to see if the protected varaible is accessed. 
        print(test.radius) # should return error to not provide access to direct variable.
    except AttributeError:
        print("This data is protected.")

main()

