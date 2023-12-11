import datetime

now = datetime.datetime.now()
Hour = now.time()
Day = now.day
Month = now.month
Year = now.year

print(now)
print(Hour)
print(Day)
print(Month)
print(Year)
# print(now)

print(now.strftime('%D'))

