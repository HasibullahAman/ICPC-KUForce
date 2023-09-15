if __name__ == '__main__':
    max_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list = [name, score]
        max_list.append(list)
    mark_list = []
    for i in max_list:
        mark_list.append(i[-1])
    lowest = min(mark_list)
    my_list_without_max = [x for x in mark_list if x != lowest]
    second_lowest = min(my_list_without_max)
    result_list = []
    for i in max_list:
        if i[-1] == float(second_lowest):
            result_list.append(i[0])
    result_list.sort(reverse=False)
    for i in result_list:
        print(i)






