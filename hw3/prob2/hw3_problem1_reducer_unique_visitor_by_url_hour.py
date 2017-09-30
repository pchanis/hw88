#! /usr/local/bin/python

import sys
import StringIO

NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

previous_hour = None
previous_usr = None
previous_url = None
count = 0
i = 0


for line in sys.stdin:
    line = line.strip(NEW_LINE_CHAR)
    url, value = line.split(TAB_CHAR)
    hour, usr = value.split(",")
    i += 1
    if i > 1:
        if url == previous_url:
            if hour == previous_hour and usr != previous_usr:
                count += 1
            if hour != previous_hour:
                count += 1
                print url + TAB_CHAR + previous_hour + TAB_CHAR + str(count)
                count = 0
        if url != previous_url and previous_url:
            count += 1
            print previous_url + TAB_CHAR + previous_hour + TAB_CHAR + str(count)
            count = 0
    previous_hour = hour
    previous_usr = usr
    previous_url = url
count += 1
print url + TAB_CHAR + previous_hour + TAB_CHAR + str(count)






