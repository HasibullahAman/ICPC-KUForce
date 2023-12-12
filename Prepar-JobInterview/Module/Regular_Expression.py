import re

txt = 'the rain is spain'

# find = re.findall("^the.*spain$",txt)
# find = re.findall('portugal', txt)

# for chick and control with space
# find = re.search('\s', txt)

# search for word in text
find = re.search('Protugal', txt)

print(find)
