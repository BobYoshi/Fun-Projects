# The following code calculates your age in years, months and days.

import datetime

day = int(input("What day were you born in? "))
month = int(input("What month were you born in? "))
year = int(input("What year were you born in? "))

now = datetime.datetime.now()

nowYear = now.year
months_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if now.year % 4 == 0:
    if now.year % 100 == 0:
        if now.year % 400 == 0:
            months_list[1] = 29

thisMonth = months_list[now.month - 1]
lastMonth = months_list[now.month -2]
year1 = nowYear - year

if month > now.month:
    year1 -= 1
    month1 = 12 - (month - now.month)
else:
    month1 = now.month - month

if day > now.day and month == now.month:
    year1 -= 1
    month1 = 11
    day1 = 31 - (day - now.day)
elif day > now.day:
    month1 -= 1
    day1 = lastMonth - (day - now.day)
elif day < now.day:
    day1 = now.day - day
else:
    day1 = 0

var1 = var2 = var3 = "s"

if year1 == 1:
    var1 = ""
if month1 == 1:
    var2 = ""
if day1 == 1:
    var3 = ""

print(f"You are {year1} year{var1}, {month1} month{var2} and {day1} day{var3} old.")

if day == now.day and month == now.month:
    print("Wait! That means it is your birthday today! HAPPY BIRTHDAY!")
