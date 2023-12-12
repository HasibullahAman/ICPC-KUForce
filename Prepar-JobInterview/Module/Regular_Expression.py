import re

txt = 'the rain is spain'

# find = re.findall("^the.*spain$",txt)
# find = re.findall('portugal', txt)

# for chick and control with space
# find = re.search('\s', txt)

# search for word in text
find = re.search('Protugal', txt)

# if I want to split the text and retrieve a list
catch = re.split('\s', txt)

for i in catch:
    # print(i)
    pass
# print(catch)
# print(find)

x = re.split("\s", txt, 6)
# print(x)


replac = re.sub('\s', "_", txt, 3)


# print(replac)

# text = 'the rain is 89spain'
# find = re.search('[a-z]?[0-9]spain$',text)
# print(find.span())


class CheckPass:
    def __init__(self, userID, userName, userPassword, userHint):
        self.userID = userID
        self.userName = userName
        self.userPassword = userPassword
        self.userHint = userHint

    def userIDAssign(self):
        pass
        self.userIDList = []
        self.userID = 1
        for i in range(len(self.userIDList)):
            if self.userIDList[i] == self.userID:
                self.userID += 1
            else:
                self.userIDList.append(self.userID)



    def check(self):
        pass



















