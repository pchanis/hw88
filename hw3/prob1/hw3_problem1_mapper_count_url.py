#! /usr/local/bin/python

import sys

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

for line in sys.stdin:
    values = {}
    line = line.strip(NEW_LINE_CHAR)
    values = line.split(" ")
    url = values[2]
    print(url + TAB_CHAR + str(1))



