# Shantel Williams
# 12\12\2023

# Medium Challenge: Functional Data Transformation
# You are given a list of dictionaries. Each dictionary represents a book with the following keys: 'title', 'author', and 'pages'. 
# Your task is to use functional programming to transform this list to contain the titles of books that have more than a specified number of pages.

# Define a function titles_of_long_books(book_list, min_pages) that:
# Filters the list to retain books with more than min_pages.
# Maps the filtered list to extract only the title of each book.
# Returns a list of titles of the filtered books.
# The function should achieve this using Python’s filter() and map() functions. Try to chain these functions together.

# books = [
#     {'title': 'Book A', 'author': 'Author 1', 'pages': 150},
#     {'title': 'Book B', 'author': 'Author 2', 'pages': 500},
#     {'title': 'Book C', 'author': 'Author 3', 'pages': 200},
#     {'title': 'Book D', 'author': 'Author 4', 'pages': 50}
# ]
# min_pages_sample = 200
def titles_of_long_books(book_list, min_pages):

    more_than_min = lambda alist: alist['pages'] > min_pages # lambda function to grab books where pages ar over min pages
    greater_than  = list(filter(more_than_min, book_list)) # filters books over min pages
    

    title_only = lambda newList: newList['title'] # lambda function to grab books where pages ar over min pages
    completed = list(map(title_only, greater_than)) # map to grab title from filtered list
    return completed

def main():
    books = [{'title': 'Book A', 'author': 'Author 1', 'pages': 150}, {'title': 'Book B', 'author': 'Author 2', 'pages': 500},{'title': 'Book C', 'author': 'Author 3', 'pages': 200},
        {'title': 'Book D', 'author': 'Author 4', 'pages': 50},{'title': 'Book E', 'author': 'Author 2', 'pages': 350},{'title': 'Book F', 'author': 'Author 5', 'pages': 600}]
    
    min_pages_sample = 200
    print(titles_of_long_books(books, min_pages_sample))

main()