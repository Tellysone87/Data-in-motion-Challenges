 # Date: 9/15/2023
 # Author: Shantel Williams

# Problem: Given a list of client emails, create a function that takes in the list as an argument 
# and returns a new list with only the domain of each email. This was inspired by an actual problem I did at work recently.

# clients = ['brucewayne@gotham.com', 
# 'homer_simpson@springfieldnuclear.com', 
# 'hank_hill@arlenpropane.com', 
# 'petergriffin@pawtucketbrewery.com']
# Example:

# get_domains(clients) = ['gotham.com', 'springfieldnuclear.com', 'arlenpropane.com', 'pawtucketbrewery.com']
# Hint: Try using regex
from re import split

def get_domains(some_list):
    return [split('@',domain)[1] for domain in some_list]


def main():
    clients = ['brucewayne@gotham.com', 
    'homer_simpson@springfieldnuclear.com', 
    'hank_hill@arlenpropane.com', 
    'petergriffin@pawtucketbrewery.com']

    test =  get_domains(clients) 
    print(test)

main()