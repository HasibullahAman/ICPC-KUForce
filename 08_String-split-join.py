def split_and_join(line):
    myline = line.split()
    result = "-".join(myline)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


