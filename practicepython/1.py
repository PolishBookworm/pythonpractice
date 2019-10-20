from datetime import datetime, timedelta

name = input('Hi! What is your name?\n')
age = int(input('OK. How old are you?\n'))
now = datetime.now()
now = int(now.year)
birth = now - age
result = birth + 100
print('You are going to be 100 in...' + str(result))