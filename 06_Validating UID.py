
import re
for i in range(int(input("Enter the number of testCase: "))):
    sample = input()
    if re.search(r'^[a-zA-Z0-9]{10}',sample):
        pass
    else:
        print("Invalid")
