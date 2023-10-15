# Date: 9/8/2023
# Author: Shantel Williams

# Given a person variable:
# person = [[“name”, “Bruce”], [“job”, “Batman”], [“city”, “Gotham”]]

# Create a dictionary called answer , that makes each first item in each list a key 
# and the second item a corresponding value. This is the end goal:

# {‘name’: ‘Bruce’, ‘job’: ‘Batman’, ‘city’: ‘Gotham’}

def create_dictionary(person_list):
   answer = {}

   for each_list in person_list:
       answer[each_list[0]] = each_list[1]
   return answer

def main():
    person = [["name", "Bruce"], ["job", "Batman"], ["city", "Gotham"]]
    test = create_dictionary(person)
    print(test)
                                                    


main()