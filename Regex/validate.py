import re
email = input("enter Your Email Address: ")
if re.search(r'^[^@]+@[^#@]+\.com$',email):
    print("Valid")
else:
    print("invalid")
