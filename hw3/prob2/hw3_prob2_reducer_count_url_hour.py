#! /usr/local/bin/python

import sys
from collections import defaultdict

NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

previous_url = None
previous_hour = None
previous_ct = 0
count = 0

for line in sys.stdin:
    line = line.strip(NEW_LINE_CHAR)
    hour, values = line.split(TAB_CHAR)
    url, ct = values.split(",")
    if hour == previous_hour or previous_hour is None:
        if url != previous_url or previous_url is None:
            count = count + int(ct)
    if hour != previous_hour and previous_hour is not None:
        print(previous_hour + TAB_CHAR + str(count))
        count = 1
    previous_url = url
    previous_hour = hour
    previous_ct = ct
print previous_hour + TAB_CHAR + str(count)






