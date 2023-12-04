import re
import sys
import datetime

content = ''
with open('input4.txt') as handle:
    content = sorted(handle.read().strip().split("\n"))

regex_guard_id = re.compile("Guard #(\d+) begins shift")
regex_datetime = re.compile("\[(.+)\]")

guards = {}
guard = None
state = 'awake'
top_sleeper = None

i = 0

for line in content:
    match = regex_datetime.match(line)
    datetime_match = match.group(1)

    line_datetime = datetime.datetime.strptime(datetime_match+":00", "%Y-%m-%d %H:%M:%S")

    match = regex_guard_id.search(line)
    if match:
        guard_id = match.group(1) 

        try:
            guard = guards[guard_id]
        except KeyError:
            guard = {'total': 0, 'id': guard_id, 'minutes': []}
            guards[guard_id] = guard

    if 'falls asleep' in line:
        start = line_datetime
    
    if 'wakes up' in line:
        curr = start
        while curr < line_datetime:
            if curr.hour == 0:
                guard['minutes'].append(curr.minute)

            curr += datetime.timedelta(minutes=1)

top_minute = -1
top_minute_count = 0
top_guard = None

for guard in guards.values():
    for i in range(60):
        minute_count = guard['minutes'].count(i)

        if minute_count > top_minute_count:
            top_minute = i
            top_minute_count = minute_count
            top_guard = guard
    

print("Guard {:s} is asleep at minute {:d} pretty often: {:d}".format(
    top_guard['id'],
    top_minute,
    int(top_guard['id']) * top_minute
))
