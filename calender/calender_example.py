
import calendar
import datetime



# obj = calendar.Calendar()

# for day in obj.itermonthdays(2020, 1):
year = 2020
month = 7
print(calendar.monthrange(year, month))
num_days = calendar.monthrange(year, month)[1]
print(calendar.monthrange(year, month)[1])
print(num_days)
for day in range(1, num_days+1):
    day_obj = datetime.date(year, month, day)
    print(day_obj)
