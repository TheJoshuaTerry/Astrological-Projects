from StarSigns import *
print('I will be calculating your Horoscope and Zodiac,\nHowever for me to do that, I will need to obtain some information from you.')
#Year input
year = int(input('First I Will need to know what year you where born? '))
while year not in years:
    year = int(input('I am unable to calculate the given year, please enter a year between 1924 and 2031 '))

print('')

#Month input
month = int(input('Next I will need the month were you born? '))
    
while month > 12:
    month = int(input('Invalid month, Please enter a number Between 1 and 12? '))

print('')
#Day input
day = int(input('and Lastly I will need the day? '))
if month in short:
    if year not in leap: 
        while day > 28:
            day = int(input('Invalid day of the month, Please enter a number Between 1 and 28? '))
    elif year in leap:
        while day > 29:
            day = int(input('Invalid day of the month, Please enter a number Between 1 and 29? '))
elif month in med:
    while day > 30:
        day = int(input('Invalid day of the month, Please enter a number Between 1 and 30? '))
elif month in long:
    while day > 31:
        day = int(input('Invalid day of the month, Please enter a number Between 1 and 31? '))
mon = 0
if month == 1:
    mon = 'January,'
elif month == 2:
    mon = 'Febuary,'
elif month == 3:
    mon = 'March,'
elif month == 4:
    mon = 'April,'
elif month == 5:
    mon = 'May,'
elif month == 6:
    mon = 'June,'
elif month == 7:
    mon = 'July,'
elif month == 8:
    mon = 'August,'
elif month == 9:
    mon = 'September,'
elif month == 10:
    mon = 'October,'
elif month == 11:
    mon = 'November,'
elif month == 12:
    mon = 'December,'

dys = 0
if day == 1 or day == 21 or day == 31:
    dys = 'st'
elif day == 2 or day == 22 or day == 32:
    dys = 'nd'
elif day == 3 or day == 23:
    dys = 'rd'
elif day >= 4 and day <= 20:
    dys = 'th'
elif day >= 24 and day <= 29:
    dys = 'th'
days = str(day) + str(dys)
z = zodiac(year)
h = horoscope(month, day)
#Outputs
'''
print('\nSince you were born in the year', year, 'your Zodiac sign is the')
print(zodiac(year))
print('\nand given that you were born on the', days, 'of', mon, 'You star sign is\n')
print(horoscope(month, day))
'''