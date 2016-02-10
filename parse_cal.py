# Needs python-icalendar

from icalendar import Calendar, Event
import datetime
import pytz
import urllib2
import getopt
import sys


url = ""
days = 7

def usage():
    print("ICal watcher / report emailer by <marcus@marcus-povey.co.uk>");
    print;
    print("Usage:");
    print("\t./parse_cal -u icalurl [-d days=7]");

def main():
	
	global url
	global days	

	try:
		opts, args = getopt.getopt(sys.argv[1:], "u:d:h", ["help"])
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit()

	for o, a in opts:
		if o == "-u":
			url = a
		elif o == "-d":
			days = int(a)
		elif o in ("-h", "--help"):
			usage()
			sys.exit()
		else:
			usage()
			sys.exit()    
	
	if len(url) == 0:
		usage();
		sys.exit()
	
	response = urllib2.urlopen(url)

	#g = open('test.ical','rb')
	#gcal = Calendar.from_ical(g.read())
	gcal = Calendar.from_ical(response.read())
 
	present = datetime.datetime.now()
	localtz = pytz.timezone('Europe/London')
 
	d = datetime.timedelta(days)

	for component in gcal.walk():
		if component.name == "VEVENT":
	      		if (component.get('dtend')).dt >= localtz.localize(present):
				if (component.get('dtstart')).dt >= localtz.localize(present) and (component.get('dtstart')).dt < localtz.localize(present + d):
					print " * " + component.get('summary')
					print " \t " +str((component.get('dtstart')).dt.strftime("%Y-%m-%d %H:%M")) + " - " + str((component.get('dtend')).dt.strftime("%Y-%m-%d %H:%M"))
      					if component.get('location') != None:
						print " \t " + component.get('location')
					if component.get('url') != None:
						print " \t " + component.get('url')
			#print (component.get('dtstamp')).dt
	#g.close()


if __name__ == "__main__":
    main()
