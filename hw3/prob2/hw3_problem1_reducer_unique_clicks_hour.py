#! /usr/local/bin/python

import sys
import StringIO

NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

previous_hour = None
previous_url = None
previous_usr = None
previous_clicks = None
count = 0
i = 0


print "unique clicks by usr by hour"
for line in sys.stdin:
    line = line.strip(NEW_LINE_CHAR)
    url, value = line.split(TAB_CHAR)
    hour, usr, clicks = value.split(",")
    i += 1
    if i > 1:
        if url == previous_url:
            if hour == previous_hour and usr == previous_usr:
                count += int(previous_clicks)
            if hour != previous_hour or usr != previous_usr:
                count += int(previous_clicks)
                print url + TAB_CHAR + previous_hour + TAB_CHAR + previous_usr + TAB_CHAR + str(count)
                count = 0
        if url != previous_url:
            count += int(previous_clicks)
            print previous_url + TAB_CHAR + previous_hour + TAB_CHAR + previous_usr + TAB_CHAR + str(count)
            count = 0
    previous_hour = hour
    previous_usr = usr
    previous_url = url
    previous_clicks = int(clicks)
count += int(previous_clicks)
print url + TAB_CHAR + previous_hour + TAB_CHAR + previous_usr + TAB_CHAR + str(count)





