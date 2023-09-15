n = int(input("enter the number of student: "))
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
mark = student_marks[query_name]
print(format(sum(mark)/3, '.2f'))