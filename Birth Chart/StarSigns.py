#Star Sign Personalities
Aries = 'Aries: (March 21 - April 19)\nThe first sign of the zodiac, Aries loves to be number one. Naturally, this dynamic fire sign is no stranger to competition. \nBold and ambitious, Aries dives headfirst into even the most challenging situations—and they\'ll make sure they always \ncome out on top!'
Taurus = 'Taurus: (April 20 - May 20)\nWhat sign is more likely to take a six-hour bath, followed by a luxurious Swedish massage and decadent dessert spread? Why \nTaurus, of course! Taurus is an earth sign represented by the bull. Like their celestial spirit animal, Taureans enjoy \nrelaxing in serene, bucolic environments surrounded by soft sounds, soothing aromas, \nand succulent flavors'
Gemini = 'Gemini: (May 21 - June 20)\nHave you ever been so busy that you wished you could clone yourself just to get everything done? That\'s the Gemini experience \nin a nutshell. Spontaneous, playful, and adorably erratic, Gemini is driven by its insatiable curiosity. Appropriately \nsymbolized by the celestial twins, this air sign was interested in so many pursuits \nthat it had to double itself. You know, NBD!'
Cancer = 'Cancer: (June 21 - July 22)\nRepresented by the crab, Cancer seamlessly weaves between the sea and shore representing Cancer’s ability to exist in both \nemotional and material realms. Cancers are highly intuitive and their psychic abilities manifest in tangible spaces. \nBut—just like the hard-shelled crustaceans—this water sign is willing to do whatever it \ntakes to protect itself emotionally. In order to get to know this sign, you\'re going to need to \nestablish trust!'
Leo = 'Leo: (July 23 - August 22)\nRoll out the red carpet because Leo has arrived. Passionate, loyal, and infamously dramatic, Leo is represented by the lion \nand these spirited fire signs are the kings and queens of the celestial jungle. They\'re delighted to embrace their royal \nstatus: Vivacious, theatrical, and fiery, Leos love to bask in the spotlight and \ncelebrate… well, themselves.'
Virgo = 'Virgo: (August 23 - September 22)\nYou know the expression, "if you want something done, give it to a busy person?" Well, that definitely is the Virgo \nanthem. Virgos are logical, practical, and systematic in their approach to life. Virgo is an earth sign historically represented \nby the goddess of wheat and agriculture, an association that speaks to Virgo\'s \ndeep-rooted presence in the material world. This earth sign is a perfectionist at heart and \nisn’t afraid to improve skills through diligent and consistent practice.'
Libra = 'Libra: (September 23 - October 22)\nBalance, harmony, and justice define Libra energy. As a cardinal air sign, Libra is represented by the scales \n(interestingly, the only inanimate object of the zodiac), an association that reflects Libra\'s fixation on establishing equilibrium. \nLibra is obsessed with symmetry and strives to create equilibrium in all areas \nof life — especially when it comes to matters of the heart.'
Scorpio = 'Scorpio: (October 23 - November 21)\nElusive and mysterious, Scorpio is one of the most misunderstood signs of the zodiac. Scorpio is a water sign that \nuses emotional energy as fuel, cultivating powerful wisdom through both the physical and unseen realms. In fact, Scorpio \nderives its extraordinary courage from its psychic abilities, which is what makes this \nsign one of the most complicated, dynamic signs of the zodiac.'
Sagittarius = 'Sagittarius: (November 22 - December 21)\nOh, the places Sagittarius goes! But… actually. This fire sign knows no bounds. Represented by the archer, \nSagittarians are always on a quest for knowledge. The last fire sign of the zodiac, Sagittarius launches its many pursuits \nlike blazing arrows, chasing after geographical, intellectual, and spiritual adventures.'
Capricorn = 'Capricorn: (December 22 - January 19)\nWhat is the most valuable resource? For Capricorn, the answer is clear: Time. Capricorn is climbing the mountain \nstraight to the top and knows that patience, perseverance, and dedication is the only way to scale. The last earth sign \nof the zodiac, Capricorn, is represented by the sea-goat, a mythological creature with \nthe body of a goat and the tail of a fish. Accordingly, Capricorns are skilled at navigating \nboth the material and emotional realms.'
Aquarius = 'Aquarius: (January 20 - February 18)\nDespite the "aqua" in its name, Aquarius is actually the last air sign of the zodiac. Innovative, progressive, and \nshamelessly revolutionary, Aquarius is represented by the water bearer, the mystical healer who bestows water, or life, \nupon the land. Accordingly, Aquarius is the most humanitarian astrological sign. At \nthe end of the day, Aquarius is dedicated to making the world a better place.'
Pisces = 'Pisces: (February 19 - March 20)\nIf you looked up the word "psychic" in the dictionary, there would definitely be a picture of Pisces next to it. \nPisces is the most intuitive, sensitive, and empathetic sign of the entire zodiac — and that’s because it’s the last of the last. \nAs the final sign, Pisces has absorbed every lesson — the joys and the pain, the \nhopes and the fears — learned by all of the other signs. It\'s symbolized by two fish swimming \nin opposite directions, representing the constant division of Pisces\' attention between fantasy and reality.'

#Zodiac Traits
Rat = 'Rat:\nQuick-witted, Resourceful, Versatile, Kind.'
Ox = 'Ox:\nDiligent, Dependable, Strong, Determined.'
Tiger = 'Tiger:\nQuick-witted, Resourceful, Versatile, Kind.'
Rabbit = 'Rabbit:\nQuiet, Elegant, Kind, Responsible.'
Dragon = 'Dragon:\nConfident, Intelligent, Enthusiastic.'
Snake = 'Snake:\nEnigmatic, Intelligent, Wise.'
Horse = 'Horse:\nAnimated, Active, Energetic.'
Goat = 'goat:\nCalm, Gentle, Sympathetic.'
Monkey = 'Monkey:\nSharp, Smart, Curious.'
Rooster = 'Rooster:\nObservant, Hardworking, Courageous.'
Dog = 'Dog\nLovely, Honest, Prudent.'
Pig = 'Pig:\nCompassionate, Generous, Diligent.'


def horoscope(m, d):
    if m == 1 and 20 <= d <= 31 or m == 2 and 1 <= d <= 18:
        return Aquarius
    elif m == 2 and 19 <= d <= 31 or m == 3 and 1 <= d <= 20:
        return Pisces
    elif m == 3 and 21 <= d <= 31 or m == 4 and 1 <= d <= 19:
        return Aries
    elif m == 4 and 20 <= d <= 31 or m == 5 and 1 <= d <= 20:
        return Taurus
    elif m == 5 and 21 <= d <= 31 or m == 6 and 1 <= d <= 20:
        return Gemini
    elif m == 6 and 21 <= d <= 31 or m == 7 and 1 <= d <= 22:
        return Cancer
    elif m == 7 and 23 <= d <= 31 or m == 8 and 1 <= d <= 22:
        return Leo
    elif m == 8 and 23 <= d <= 31 or m == 9 and 1 <= d <= 22:
        return Virgo
    elif m == 9 and 23 <= d <= 31 or m == 10 and 1 <= d <= 22:
        return Libra
    elif m == 10 and 23 <= d <= 31 or m == 11 and 1 <= d <= 20:
        return Scorpio
    elif m == 11 and 23 <= d <= 31 or m == 12 and 1 <= d <= 20:
        return Sagittarius
    elif m == 12 and 21 <= d <= 31 or m == 1 and 1 <= d <= 19:
        return Capricorn
    return 0
    
def zodiac(y):
    if y in rat:
        return Rat
    elif y in ox:
        return Ox
    elif y in tiger:
        return Tiger
    elif y in rabbit:
        return Rabbit
    elif y in dragon:
        return Dragon
    elif y in snake:
        return Snake
    elif y in horse:
        return Horse
    elif y in goat:
        return Goat
    elif y in monkey:
        return Monkey
    elif y in rooster:
        return Rooster
    elif y in dog:
        return Dog
    elif y in pig:
        return Pig

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
1997, 1996, 1995, 1994, 1993, 1992, 1991, 1990, 1989, 1988, 1987, 1986, 1985, 1984, 1983, 1982, 1981,1980,
1979, 1978, 1977, 1976, 1975, 1974, 1973, 1972, 1971, 1970, 1969, 1968, 1967, 1966, 1965, 1964, 1963, 1962,
1961, 1960, 1959, 1958, 1957, 1956, 1955, 1954, 1953, 1952, 1951, 1950, 1949, 1948, 1947, 1946, 1945, 1944, 1943,
1942, 1941, 1940, 1939, 1938, 1937, 1936, 1935, 1934, 1933, 1932, 1931, 1930, 1929, 1928, 1927, 1926, 1925, 1924]
short = [2]
med = [4,6,9,11]
long = [1,3,5,7,8,10,12]
leap = [1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980,
1984, 1988, 1992, 1996, 2000, 2004, 2008, 2016, 2020, 2024, 2028, 2032, 2036, 2040, 2044, 2048, 2052, 2056, 2060]
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', 1 ,2, 3, 4 ,5, 6, 7, 8, 9, 10, 11, 12]

dictMonth = {
    1 : ['January', 'january', 'jan', 'Jan', 'JAN'],
    2 : ['Febuary', 'febuary', 'feb', 'Feb', 'FEB'],
    3 : ['March', 'march', 'mar', 'Mar', 'MAR',],
    4 : ['April', 'april', 'apr', 'Apr', 'APR'],
    5 : ['may', 'May', 'MAY'],
    6 : ['June', 'june', 'jun', 'Jun', 'JUN'],
    7 : ['July', 'july', 'jul', 'Jul', 'JUL'],
    8 : ['August', 'august', 'aug', 'Aug', 'AUG'],
    9 : ['September', 'september', 'sep', 'Sep', 'SEP'],
    10 : ['October', 'october', 'oct', 'Oct', 'OCT'],
    11 : ['Novemeber', 'novemeber', 'nov', 'Nov', 'NOV'],
    12 : ['December', 'december', 'dec', 'Dec', 'DEC'],
    13 : ['January', 'january', 'jan', 'Jan', 'JAN', 'Febuary', 'febuary', 'feb', 'Feb', 'FEB', 'March',
    'march', 'mar', 'Mar', 'MAR', 'April', 'april', 'apr', 'Apr', 'APR', 'may', 'May', 'MAY', 'June',
    'june', 'jun', 'Jun', 'JUN', 'July', 'july', 'jul', 'Jul', 'JUL', 'August', 'august', 'aug', 'Aug', 'AUG',
    'September', 'september', 'sep', 'Sep', 'SEP', 'October', 'october', 'oct', 'Oct', 'OCT', 'Novemeber',
    'novemeber', 'nov', 'Nov', 'NOV', 'December', 'december', 'dec', 'Dec', 'DEC'],
}

# Start of code execution

