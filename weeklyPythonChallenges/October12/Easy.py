# Shantel Williams
# 12/11/2023

# Easy Challenge: Dictionary Value Doubler
# You are given a dictionary where the keys are strings and the values are numbers. 
# Write a function double_values(d) that doubles each value in the dictionary and returns the modified dictionary.

# sample_dict = {
#     'a': 5,
#     'b': 10,
#     'c': 15
# }

def double_values(provided_dict):
    for Each_key in provided_dict:
        provided_dict[Each_key] = provided_dict.get(Each_key,0) * 2

    return provided_dict
    
def main():
    sample_dict = {
    'a': 5,
    'b': 10,
    'c': 15
}
    
    print(double_values(sample_dict))

main()