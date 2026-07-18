import re

resume = """
Name:Ajay
Email: ajay@gmail.com
Phone: 9876543210
Skills: Python, SQL, Machine Learning
Experience: 5 years
"""

name = re.search(r"Name:\s*(.*)", resume)
email = re.search(r"\S+@\S+", resume)
phone = re.search(r"\d{10}", resume)
skills = re.findall(r"Python|Java|SQL|Machine Learning|NLP", resume, re.I)
exp = re.search(r"(\d+)\s+years", resume)

print("Name:", name.group(1))
print("Email:", email.group())
print("Phone:", phone.group())
print("Skills:", skills)
print("Experience:", exp.group(1), "years")

if int(exp.group(1)) >= 2 and "Python" in skills:
    print("Eligible Candidate")
else:
    print("Not Eligible")
