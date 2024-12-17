def is_leap(year):
# Function to check whether the year is leap or not
# input: year (int)
# output: True or False (Boolean)
##############################
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

######Main program starts here #####
year = -1
while year != 0:
    year = int(input('What is the year? '))
    if is_leap(year):
        print('leap')
    else:
        print('not leap')