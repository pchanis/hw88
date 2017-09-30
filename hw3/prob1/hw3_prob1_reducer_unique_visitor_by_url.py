#! /usr/local/bin/python

import sys
import StringIO

NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

previous_key = None
previous_val = None
count = 0

#sys.stdin = StringIO.StringIO("s0\tu0\ns0\tu1\ns1\tu0")

for line in sys.stdin:
    line = line.strip(NEW_LINE_CHAR)
    key, value = line.split(TAB_CHAR)
    if value != previous_val or previous_val is None:
        if key == previous_key:
            count += 1
    previous_val = value
    if key != previous_key:
        if previous_key is not None:
            count += 1
            print (previous_key + TAB_CHAR + str(count))
            count = 0
        previous_key = key
print (previous_key + TAB_CHAR + str(count+1))






