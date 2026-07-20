import re

text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

match = re.match(pattern, text)

if match:
    print("Match Found")
    print("Matched Text:", match.group())
else:
    print("Match Not Found")

search = re.search(pattern, text)

if search:
    print("Search Found")
    print("Matched Text:", search.group())
    print("Position:", search.start(), "to", search.end())
else:
    print("Search Not Found")
