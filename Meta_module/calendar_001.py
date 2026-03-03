import sys
locations = sys.path
# print(locations) 
for i in locations:
    print(i)


import calendar
leap_year = calendar.leapdays(2000, 2050)
print(leap_year)

#check leap year
is_it_leap = calendar.isleap(2036)
print(is_it_leap) 

# calendar.month(year, month)
month = calendar.month(2026, 3)
print(month)
