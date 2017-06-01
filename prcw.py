

#! Python3

import datetime

# URL how to download from a file URL http://sgeek.org/download-file-using-python-over-http/
# Initialize Date and Time for today's date

now = datetime.datetime.now()

#Initialize urls
nyturl = 'http://www.nytimes.com/svc/crosswords/v2/puzzle/'
laturl = 'http://www.cruciverb.com/download.php?f='


def monthname():
	#datenames = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
	#return datenames[(now.month-1)]
	if len(str(now.month)) == 2:
		return str(now.month)
	else:
		return "0" + str(now.month)

def dayname():
	if len(str(now.day)) == 2:
		return str(now.day)
	else:
		return "0" + str(now.day)

def yearname():
	return str(now.year)[2:]


def nytpuz():
	filename = 'daily-' + str(now.year) + '-'
	filename += monthname() + '-'
	filename += dayname() + '.puz'
	return filename


def latpuz():
	return 'lat' + yearname() + monthname() + dayname() + '.puz'



#Printing out to the screen for debugging purposes

print (monthname() + " " + dayname() + " " + yearname())
print('Today\'s NYT file: ' + nytpuz())
print('Today\'s LAX file: ' + latpuz())
print('NYT URL: ' + nyturl + nytpuz())
print('LAT URL: ' + laturl + latpuz())


#def todaysnytname(date):


#def todayslatname(date):

