# Date: 7/11/2023
# Author: Shantel Williams
# pushes to github

# instructions:
# Given a list of dictionaries where each dictionary contains ‘name’ 
# and ‘date_of_birth’ of individuals, write a Python function to find the oldest person. For example:

# persons = [
# {"name": "Kedeisha", "date_of_birth": "1994-05-20"},
# {"name": "Homer", "date_of_birth": "1956-05-12"},
# {"name": "Bruce", "date_of_birth": "1915-04-07"},
# ]

# After reviewing the python docs, We will use fromisoformat() to Return a date corresponding to the date_string given. 
#This is needed to compare each date
from datetime import date 

def find_oldest_person(provided_list):
    """ Function to find the oldest person of the provided list of dicitonaries"""
   
    dates = [] # Decided to convert each date of birth into date objects and place them in a list for sorting. This list will store them for me 
    oldest = "" # setting oldest variable to a blank string until I receive my answer
    
    for person in provided_list: #loop through list of dictionaries and
        newDate = date.fromisoformat(person["date_of_birth"]) # convert dates to a date object and add it to my list
        dates.append(newDate)

    sorted_dates = sorted(dates) # puts the dates in order from lowest to highest or (oldest to most recent)

    for person in provided_list: # I then looped again to find the name corresponding to the oldest age in my list
        if person["date_of_birth"] == str(sorted_dates[0]): # this would be the date at the 0 index because my list was sorted
            oldest = person["name"] # This is our oldest person

    return oldest # return results

def main():
    persons = [{"name": "Kedeisha", "date_of_birth": "1994-05-20"}, 
{"name": "Homer", "date_of_birth": "1956-05-12"},
{"name": "Bruce", "date_of_birth": "1915-04-07"},]

    print(f"The oldest person is {find_oldest_person(persons)}.") # calling my funtion and printing it 

main()