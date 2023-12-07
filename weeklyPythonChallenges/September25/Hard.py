# Hard Challenge: HTML Tag Extractor
# HTML tags are often used to format and organize content on web pages. Your task is to write a function named extract_tags(html_string) that:

# Accepts a string html_string representing a portion of an HTML document.
# Extracts and returns all unique HTML tags (without attributes) from the string.
# The function should use regular expressions to identify and extract the tags.

# Note:
# A typical HTML tag looks like <tagname>...</tagname>, and you need to extract ‘tagname’ out of it.
# Some tags might also be self-closing like <tagname/>.

# html1 = "<div><p>Some text here</p></div><a href='#'>Link</a>"
# html2 = "<header><meta charset='UTF-8'/><title>Page Title</title></header>"

import re

def extract_tags(html_string):
    list_all = re.findall()


    print(list_all)

def main():
    html1 = "<div><p>Some text here</p></div><a href='#'>Link</a>"
    html2 = "<header><meta charset='UTF-8'/><title>Page Title</title></header>"

    print(extract_tags(html1))
    print(extract_tags(html2))

main()