# Four Rule

# we use open function for open the file as every method that have
import re

# as this syntax
# file = open('nameOfTheFile','rt')

'''
 1- we use 'r' for read, Error if file not exist!
 2- we use 'w' for write, if file not Exist it will be created!
 3- we use 'a' for appending, if file not exist it going to create!
 4- we use 'x' for creating, if file exist it going to get Error!
'''

# we have two type data read, one for image as binary and second for txt!
'''
    1- 't' for txt
    2- 'b' for binary
'''
#
# file = open('demoFile.txt', 'rt')
# text = open(file.read())
# for i in file.readline():
#     print(i)


# print(re.findall(['Hasibullah Aman'], file.read()))


import os

os.remove('demoFile.txt')
