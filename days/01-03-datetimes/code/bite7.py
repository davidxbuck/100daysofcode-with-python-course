'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
import os
import re
import urllib.request
from datetime import datetime

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
#    Both of these options produce the same output, but the regex would work if the log format changed
#    match = line.split()[1]
#    date = datetime.strptime(match, '%Y-%m-%dT%H:%M:%S')
    match = re.search(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}', line)

    date = datetime.strptime(match.group(), '%Y-%m-%dT%H:%M:%S')
    return date


def time_between_shutdowns(log):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the
       timedelta between the first and last one.
       Return this datetime.timedelta object.'''
    shutdowns = list(filter(lambda x: SHUTDOWN_EVENT in x, log))
    first = convert_to_datetime(shutdowns[0])
    last = convert_to_datetime(shutdowns[-1])
    difference = last - first
    return difference

print(time_between_shutdowns(loglines))
