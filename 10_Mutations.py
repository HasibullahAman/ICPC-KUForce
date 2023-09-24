def mutate_string(string, position, character):
    mystring = list(string)
    mystring[position] = character
    mystring = "".join(mystring)
    return mystring
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)