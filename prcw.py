

#! Python3

import datetime


# Initialize Date and Time for today's date

now = datetime.datetime.now()

day = str(now.day)
month = str(now.month)
year = str(now.year)

# Function to return the monthname from the month number

def monthname():
	datenames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	return datenames[(now.month-1)]




print('day: ' + day + 'month: ' + month + 'year: ' + year)

print (monthname())


#def todaysnytname(date):


#def todayslatname(date):

