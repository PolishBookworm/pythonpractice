# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.
from datetime import datetime, timedelta

name = input('Hi! What is your name?\n')
age = float(input('OK. How old are you?\n'))
now = datetime.now()
now = int(now.year)
birth = now - age
result = birth + 100
print(name + ', you are going to be 100 in the year... ' + str(result))