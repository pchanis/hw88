#! /usr/local/bin/python

import sys
import StringIO

NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

previous_key = None
previous_usr = None
previous_clicks = None
count = 0

for line in sys.stdin:
    line = line.strip(NEW_LINE_CHAR)
    key, value = line.split(TAB_CHAR)
    usr, clicks = value.split(",")
    if key == previous_key or previous_key is None:
        if usr == previous_usr or previous_usr is None:
            count = int(count) + int(clicks)
        if usr != previous_usr and previous_usr is not None:
            print key + TAB_CHAR + previous_usr + TAB_CHAR + str(count)
            count = clicks
        previous_usr = usr
        previous_clicks = clicks
    if key != previous_key and previous_key is not None:
        print previous_key + TAB_CHAR + previous_usr + TAB_CHAR + str(count)
        count = clicks
    previous_usr = usr
    previous_clicks = clicks
    previous_key = key
print previous_key + TAB_CHAR + previous_usr + TAB_CHAR + str(count)






