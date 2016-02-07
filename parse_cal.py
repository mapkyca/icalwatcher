# Needs python-icalendar

from icalendar import Calendar, Event
from datetime import datetime
import urllib2
import getopt
import sys


url = ""

def usage():
    print("ICal watcher / report emailer by <marcus@marcus-povey.co.uk>");
    print;
    print("Usage:");
    print("\t./parse_cal -u icalurl");

def main():
	
	global url
	
	try:
		opts, args = getopt.getopt(sys.argv[1:], "u:h", ["help"])
	except getopt.GetoptError, err:
		print str(err)
		usage()
		sys.exit()

	for o, a in opts:
		if o == "-u":
			url = a
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

	for component in gcal.walk():
		if component.name == "VEVENT":
			print component.get('summary')
			print component.get('dtstart')
			print component.get('dtend')
			print component.get('dtstamp')
	#g.close()


if __name__ == "__main__":
    main()
