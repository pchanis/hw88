#! /usr/local/bin/python

import sys
import datetime

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

for line in sys.stdin:
    values = {}
    line = line.strip(NEW_LINE_CHAR)
    values = line.split(" ")
    url = values[2]
    usr = values[3]
    dt = datetime.datetime.strptime(values[0] + " " + values[1], "%Y-%m-%d %H:%M:%S.%f")
    dt_hour = dt.replace(microsecond=0,second=0,minute=0)
    print(url + TAB_CHAR + str(dt_hour) + "," + usr + "," + str(1))
