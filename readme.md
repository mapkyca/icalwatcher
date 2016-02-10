# Python upcoming events mailer

Point it at an ical list and it'll tell you what's coming up in the next x days (default 7)

## Mailing this (if there's something coming up)

Assumes bsd-mailx

python parse_cal.py -u 'https://feed' -d 15 | mail -E -s "Events for the next 15 day" somebody@example.com

