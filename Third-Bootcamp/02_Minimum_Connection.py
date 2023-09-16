
for number_of_testCase in range(int(input("Enter the number of test Case: "))):
    listOfPoint_Conct = list(map(int, input("Enter the number of Point and Connection: ")))
    number_ofPoint = listOfPoint_Conct[0]
    number_ofConnection = listOfPoint_Conct[1]
    for each_con in range(number_ofConnection):
        list_con_cost = list(map(int, input("Enter the con pair and cost: ")))
        first_point = list_con_cost[0]
        second_point = list_con_cost[1]
        cost = list_con_cost[2]

