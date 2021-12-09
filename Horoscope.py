def horoscope(m, d):
    if m == 1 and 20 <= d <= 31 or m == 2 and 1 <= d <= 18:
        return print('Aquarius')
    elif m == 2 and 19 <= d <= 31 or m == 3 and 1 <= d <= 20:
        return print('Pisces')
    elif m == 3 and 21 <= d <= 31 or m == 4 and 1 <= d <= 19:
        return print('Aries')
    elif m == 4 and 20 <= d <= 31 or m == 5 and 1 <= d <= 20:
        return print('Taurus')
    elif m == 5 and 21 <= d <= 31 or m == 6 and 1 <= d <= 20:
        return print('Gemini')
    elif m == 6 and 21 <= d <= 31 or m == 7 and 1 <= d <= 22:
        return print('Cancer')
    elif m == 7 and 23 <= d <= 31 or m == 8 and 1 <= d <= 22:
        return print('Leo')
    elif m == 8 and 23 <= d <= 31 or m == 9 and 1 <= d <= 22:
        return print('Virgo')
    elif m == 9 and 23 <= d <= 31 or m == 10 and 1 <= d <= 22:
        return print('Libra')
    elif m == 10 and 23 <= d <= 31 or m == 11 and 1 <= d <= 20:
        return print('Scorpio')
    elif m == 11 and 23 <= d <= 31 or m == 12 and 1 <= d <= 20:
        return print('Sagittarius')
    elif m == 12 and 21 <= d <= 31 or m == 1 and 1 <= d <= 19:
        return print('Capricorn')
    
def zodiac(y):
    if y in rat:
        print('Rat')
    elif y in ox:
        print("Ox")
    elif y in tiger:
        print('Tiger')
    elif y in rabbit:
        print('Rabbit')
    elif y in dragon:
        print('Dragon')
    elif y in snake:
        print('Snake')
    elif y in horse:
        print('Horse')
    elif y in goat:
        print('Goat')
    elif y in monkey:
        print('Monkey')
    elif y in rooster:
        print('Rooster')
    elif y in dog:
        print('Dog')
    elif y in pig:
        print('Pig')

rat = [1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020]
ox = [1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021]
tiger = [1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022]
rabbit = [1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023]
dragon = [1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024]
snake = [1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025]
horse = [1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026]
goat = [1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027]
monkey = [1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028]
rooster = [1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029]
dog = [1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030]
pig = [1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031]
years = [2031, 2030, 2029, 2028, 2027, 2026, 2025, 2024, 2023, 2022 ,2021, 2020, 2019, 2018, 2017, 2016,
2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006, 2005, 2004, 2003, 2002, 2001, 2000, 1999, 1998,
1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983,
1982, 1981,1980, 1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963,
1962, 1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943,
1942, 1941, 1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924]
short = [2]
med = [4,6,9,11]
long = [1,3,5,7,8,10,12]
leap = [1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]
str_months = ['january', 'febuary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'novemeber', 'december', 'jan', 'Jan',
'feb', 'Feb', 'mar', 'Mar', 'apr', 'Apr', 'may', 'May', 'jun', 'Jun', 'jul', 'Jul', 'aug', 'Aug', 'sep', 'Sep', 'oct', 'Oct', 'nov', 'Nov',
'dec', 'Dec', 'DEC', 'NOV', 'OCT', 'SEP', 'AUG', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 1 ,2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12]

# Start of code execution

print('I will be calculating your Horoscope and Zodiac,\nHowever for me to do that, I will need to obtain some information from you.')
year = int(input('First I Will need to know what year you where born? '))
while year not in years:
    year = int(input('I am unable to calculate the given year, please enter a year between 1924 and 2031 '))

print('')

month = int(input('Next I will need the month were you born? '))
while month > 12:
    month = int(input('Invalid month, Please enter a number Between 1 and 12? '))
print('')

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
    mon = 'January'
elif month == 2:
    mon = 'Febuary'
elif month == 3:
    mon = 'March'
elif month == 4:
    mon = 'April'
elif month == 5:
    mon = 'May'
elif month == 6:
    mon = 'June'
elif month == 7:
    mon = 'July'
elif month == 8:
    mon = 'August'
elif month == 9:
    mon = 'September'
elif month == 10:
    mon = 'October'
elif month == 11:
    mon = 'November'
elif month == 12:
    mon = 'December'

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
print('Since you were born in', year, 'your Zodiac sign is a(n)')
zodiac(year), 
print('and given that you were born in', mon, 'on the', days, 'day, You are a(n)')
horoscope(month, day)