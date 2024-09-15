def day_of(start_day, is_leap_year, date):
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    month_days = [31, 29 if is_leap_year else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start_index = days.index(start_day)

    total_days = 0
    for i in range(date[0] - 1):
        total_days += month_days[i]
    total_days += date[1] - 1

    current_day_index = (start_index + total_days) % 7
    return days[current_day_index]


def count_weekdays(start_day, is_leap_year):
    days_in_month = [31, 28 if not is_leap_year else 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    weekdays_count = [0] * 7

    days_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    start_day_index = days_map[start_day]

    day_of_week = start_day_index
    for days_in_curr_month in days_in_month:
        for _ in range(days_in_curr_month):
            weekdays_count[day_of_week] += 1
            day_of_week = (day_of_week + 1) % 7

    return weekdays_count


n = int(input())
year = int(input())
a = [0] * n
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for i in range(0, n):
    a[i] = input().split()
    a[i][1] = months.index(a[i][1]) + 1
start_day = input()
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    is_leap_year = True
else:
    is_leap_year = False
weekday_counts = count_weekdays(start_day, is_leap_year)
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in a:
    day = day_of(start_day, is_leap_year, [int(i[1]), int(i[0])])
    weekday_counts[days.index(day)] -= 1
print(days[weekday_counts.index(max(weekday_counts))], ' ', end="")
print(days[weekday_counts.index(min(weekday_counts))], ' ')
"""
for i, day in enumerate(days):
    print(f"{day}: {weekday_counts[i]}")
n = 0
for i in weekday_counts:
    n += i
print(n)
"""