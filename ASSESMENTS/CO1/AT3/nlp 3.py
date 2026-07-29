import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
"""

def search_date():
    result = re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text)
    print("Dates Found:", result)

def search_phone():
    result = re.findall(r'\b\d{10}\b', text)
    print("Phone Numbers Found:", result)

def search_hashtag():
    result = re.findall(r'#\w+', text)
    print("Hashtags Found:", result)

def search_mention():
    result = re.findall(r'@\w+', text)
    print("Mentions Found:", result)

def search_prefix():
    word = input("Enter prefix: ")
    result = re.findall(r'\b' + word + r'\w*', text)
    print("Prefix Words Found:", result)

def search_suffix():
    word = input("Enter suffix: ")
    result = re.findall(r'\b\w*' + word + r'\b', text)
    print("Suffix Words Found:", result)


while True:
    print("\nTEXT SEARCH ENGINE")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        search_date()

    elif choice == 2:
        search_phone()

    elif choice == 3:
        search_hashtag()

    elif choice == 4:
        search_mention()

    elif choice == 5:
        search_prefix()

    elif choice == 6:
        search_suffix()

    elif choice == 7:
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
