import re

txt = 'the rain is spain'

find = re.search("^the.*spain$",txt)
print(find)