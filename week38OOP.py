# Create a Python class Car that represents a car. The car should be initialized with its make, model, and year of manufacture. 
# The class should have the following methods:

# get_details(): This method should return a string representing the details of the car in the format “make model (year)”.
# set_details(new_make, new_model, new_year): This method should set new details for the car.
# age(): This method should calculate and return the age of the car based on the current year. Assume the current year is 2023.

# To test your implementation, create a Car object with make “Toyota”, model “Corolla”, and year 2015. Update the details to make “Honda”, model “Civic”, and year 2018, and then calculate and print the age of the car.
class car:
    def __init__(self, make, model, year): # initialize instance of class car
        self.make = make 
        self.model = model
        self.year = year

    def get_details(self):
        """ This method should return a string representing the details of the car in the format “make model (year)”"""
        return f"The make is {self.make}, the model is {self.model}, and the year is {self.year}"

    def set_details(self, name_to_change, new_value):
        """ This method should set new details for the car."""
        car_value = ["make","model","year"] # make a list to check if the argument passed a correct detail name This list contains all 3 class attributes

        if name_to_change not in car_value: # check if detail  passed is a class attribute
            print("Enter a correct detail to change.") # if not display the following string
        
        if name_to_change == "make":
            self.make = new_value

        elif name_to_change == "model":
            self.model = new_value

        elif name_to_change == "year":
            self.year = new_value
       
    def age(self):
        """ This method should calculate and return the age of the car based on the current year. Assume the current year is 2023."""
        year = int(self.year)

        current_age = 2023 - year # assuming year is 2023 and subtracting the year from it 

        return current_age #return current age

def main():
    fake_car = car("smiley","happy","2013")
    details = fake_car.get_details() # will display car detail
    print(details)

    fake_car.set_details("make","laughing") # sets the make attribute to laughing
    print(fake_car.get_details()) # displays these changes

    fake_car.set_details("color","blue") # will let us know that coloe is not a class detail
    
    print(fake_car.age()) # prints age 


main()