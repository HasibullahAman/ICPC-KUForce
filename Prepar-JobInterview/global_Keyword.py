
x = 'apple'

def fruites():
    global x # in the first we declare the variable and then we assign
    x='banana'
    print(x)

fruites()
print(x)