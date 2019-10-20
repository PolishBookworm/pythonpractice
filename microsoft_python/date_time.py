###import date and time library
from datetime import datetime, timedelta

###calculating today and yesterday
today = datetime.now()
one_day = timedelta(days=1)
yesterday = today - one_day
print()
print('Today is... ' + str(today))
print()
print('Yesterday was... ' + str(yesterday))
print()

###simple date printing
now = datetime.now()
print('Day: ' + str(now.day))
print('Month: ' + str(now.month))
print('Year: ' + str(now.year))

##converting strings to dates
birthday = input('When is your birthday (dd/mm/yyyy)?\n')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Birthday: ' + str(birthday_date))
