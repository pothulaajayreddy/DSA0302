import re

reg = input("Register Number: ")
email = input("Email: ")
course = input("Course Code: ")
semester = input("Semester: ")
mobile = input("Mobile Number: ")

valid = True

if not re.fullmatch(r"\d{9}", reg):
    valid = False

if not re.fullmatch(r"\w+@saveetha\.com", email):
    valid = False

if not re.fullmatch(r"[A-Z]{3}\d{2}", course):
    valid = False

if not re.fullmatch(r"[1-8]", semester):
    valid = False

if not re.fullmatch(r"\d{10}", mobile):
    valid = False

if valid:
    print("Registration Successful")
else:
    print("Registration Failed")
