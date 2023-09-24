def print_full_name(first, last):
    result = "Hello " + first +" "+ last +"! " + "You just delved into python."
    return result

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    result =print_full_name(first_name, last_name)
    print(result)