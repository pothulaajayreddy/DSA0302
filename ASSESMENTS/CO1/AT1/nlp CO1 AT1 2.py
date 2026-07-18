import re

products = ["Laptop", "Laptop Bag", "Mouse", "Keyboard",
            "Gaming Laptop", "USB Cable"]

keyword = input("Enter product keyword: ")

matches = []

for product in products:
    if re.search(keyword, product, re.I):
        matches.append(product)

print("Matching Products:")
for p in matches:
    print(p)

print("Total Matches:", len(matches))
