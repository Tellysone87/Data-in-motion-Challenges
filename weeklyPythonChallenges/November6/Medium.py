# Shantel Williams
# 12/19/2023

# Background: Email marketing campaigns need to filter out invalid email addresses to maintain a high delivery rate.
# Problem Statement: Given a list of email addresses, write a function to filter out invalid email addresses. 
# A valid email has a username, an “@” symbol, and a domain name.

# emails = [
#     'john.doe@example.com',
#     'jane-doe@anotherexample.com',
#     'invalidemail.com',
#     'alice@examplecom',
#     'bob@website.com'
# ]
import re

def filter_emails(alist):
    pattern = "^.*@.*\..*$"

    new_list = [email for email in alist if re.search(pattern,email)]

    return new_list

def main():
    emails = [
    'john.doe@example.com',
    'jane-doe@anotherexample.com',
    'invalidemail.com',
    'alice@examplecom',
    'bob@website.com'
]
    print(filter_emails(emails))

main()