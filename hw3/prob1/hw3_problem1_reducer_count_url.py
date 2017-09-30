#! /usr/local/bin/python

import sys

NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

previous = None
count = 0

for line in sys.stdin:
    key, value = line.split(TAB_CHAR)
    if key != previous or previous is None:
        count += 1
    previous = key
print ("count" + TAB_CHAR + str(count))






