

#! Python3

import datetime


# Initialize Date and Time for today's date

now = datetime.datetime.now()

# day = str(now.day)
# month = str(now.month)
# year = str(now.year)

# Functions to return strings used by NYT and LAX in their crossword names


def monthname():
	datenames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	return datenames[(now.month-1)]


def dayname():
	if len(str(now.day)) == 2:
		return str(now.day)
	else:
		return "0" + str(now.day)

def yearname():
	return str(now.year)[2:]


# Not sure yet what the file name rules are but this is a start

print (monthname() + " " + dayname() + " " + yearname())

#def todaysnytname(date):


#def todayslatname(date):

