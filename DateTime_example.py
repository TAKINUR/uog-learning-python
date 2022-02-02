'''
    Date and time 
---------------------------
Python has a module named datetime

Commonly used classes are: 
    date class
    time class
    datetime class
    timedelta class
     

'''

from datetime import date, datetime

dt_obj = datetime.now()

# print(dt_obj) 

# cdate = date.today()

# print(cdate)

# print(cdate.year)
# print(cdate.month)
# print(cdate.day)

# print(dt_obj.hour)
# print(dt_obj.minute)
# print(dt_obj.second)
# print(dt_obj.microsecond)

# Formatting DateTime
print(dt_obj.strftime('Weekend short : %a'))
print(dt_obj.strftime('Weekend long : %A'))
print(dt_obj.strftime('Weekend number : %w'))
print('-' * 50)
print(dt_obj.strftime('Month short : %b'))
print(dt_obj.strftime('Month long : %B'))
print(dt_obj.strftime('Month number : %m'))
print('-' * 50)
print(dt_obj.strftime('Day of Month : %d'))
print(dt_obj.strftime('year without century : %y'))
print(dt_obj.strftime('year with century : %Y'))
print('-' * 50)
print(dt_obj.strftime('Full Time : %T'))
print(dt_obj.strftime('Full Date : %D'))
print('-' * 50)
print(dt_obj.strftime('Hour 24 : %H'))
print(dt_obj.strftime('Hour 12 : %I'))
print(dt_obj.strftime('AM/PM : %p'))
print(dt_obj.strftime('Minute : %M'))
print(dt_obj.strftime('Second : %S'))
print(dt_obj.strftime('Microsecond : %f'))
print('-' * 50)


print('Display Custom Format!')
print(dt_obj.strftime('%d-%m-%Y'))
print(dt_obj.strftime('%A, %m/%d/%Y'))
print(dt_obj.strftime('%A, %d-%b-%y'))
print('-' * 50)

d1 = date(year = 2000, month = 2, day = 1)
# d2 = date(year = 2011, month = 3, day = 10)
d2 = date.today()
d3 = d2 - d1

print(d3)