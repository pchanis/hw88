import sys

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

for line in sys.stdin:
    values = {}
    line = line.strip(NEW_LINE_CHAR)
    values = line.split(" ")
    print(values[2] + TAB_CHAR + str(1))



