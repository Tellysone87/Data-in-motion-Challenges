# Author: Shantel Williams
# Date: 7/7/2023

# Given the following list of emails, Write a Python function to filter out all emails that belong to the “dim.com” domain.
#
# emails = ["kedeisha@example.com", "soanli@example.com", "taamir@example.com", "shawn@dim.com", 
#           "frank@dim.com", "mikey@dim.com"],

def filter_email(email_list):
    """ A function to filter out all emails that belong to the “dim.com” domain."""

    filtered_list = [] # A list to append the emails meeting the criteria

    for email in email_list: # loop through each email in the parameters provided list
        if email.endswith('dim.com') == True: # found this endswith() string method which will return an boolean value
            filtered_list.append(email) # if True, I am adding it to the filtered list

    return filtered_list # this returns the filtered list and can then be passed as a argument value to my print function

def print_filtered_email(new_filter_list):
    """ This function will print each email in a numbered list. I will pass the filtered list as a argument """

    i = 1 # variable to keep count of index number and numbering of emails
    stop = len(new_filter_list) # varible to stop the loop

    while i <= stop: # loop through the filtered list
        print(f"{i}. {new_filter_list[i-1]}") # print the number line and email. I minus one because we are numbering the lines beginning at one.
        i +=1 # increment to avoid infinite loop

def main():
    emails = ["kedeisha@example.com", "soanli@example.com", "taamir@example.com", 
              "shawn@dim.com", "frank@dim.com", "mikey@dim.com"] # provided list for testing
    
    print_filtered_email(filter_email(emails)) # calling my print function and passing the filtered list function return value

main()