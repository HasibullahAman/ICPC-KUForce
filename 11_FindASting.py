def count_substring(string, sub_string):
    resutl = string.find(sub_string)
    if resutl == -1:
        return 0
    else:
        return resutl

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)