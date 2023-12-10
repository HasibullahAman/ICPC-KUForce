
def my_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
       return my_rec(n-1) + my_rec(n-2)



print(my_rec(8))