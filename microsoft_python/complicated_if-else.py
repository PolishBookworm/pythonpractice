###computing Canadian tax
# country = input('What is your country?\n')
# if country.lower() == 'canada':
#     province = input('What is your province?\n')
#     if province.lower() in('alberta', 'nunavut', 'yukon'):
#         ##can also use or
#         tax = 0.05
#     elif province.lower() == 'ontario':
#         tax = 0.13
#     else:
#         tax = 0.15
# else:
#     tax = 0
# print('The tax is: ' + str(tax))

###computing if you get the honour roll
gpa = float(input('What is your grade point average?\n'))
lowest_grade = float(input('What is your lowest grade?\n'))
if gpa >= .85 and lowest_grade >= .70:
    honour_roll = True
else:
    honour_roll = False
if honour_roll:
    print('Well done!')