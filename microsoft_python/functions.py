###print the cuurent time
# from datetime import datetime
# def print_time(task_name):
#     print(task_name)
#     print(datetime.now())
#     print()

# first_name = 'Susan'
# print_time('first name assigned')

# for x in range(0,10):
#     print(x)
# print_time('loop completed')

###initials
##gets initials
def get_initial(name):
    initial = name[0:1].upper()
    return initial
first_name = input('What is your first name?\n')
last_name = input('What is your last name?\n')
print(f'Your initials are: {get_initial(first_name)}{get_initial(last_name)}')