import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"

prog = "hw2_3"
desc = "Generate test log files of the form <timestamp> <userid> <url>"

parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--outfile','-f',default='_events.txt')
parser.add_argument('--user-count','-uc',default=10, type=int)
parser.add_argument('--event-count-user-url','-uuc',default=10, type=int)
parser.add_argument('--url-file','-uf')
parser.add.argument('--thread-count', '-tc', default=4, type=int)

parsed_args = parser.parse_args()
outfile = parsed_args.outfile
user_count = parsed_args.user_count
events_per_user_url = parsed_args.event_count_user_url
url_list_file = parsed_args.url_file

def generate_event_record():
    line_val = ""
    for column_no in range(column_count):
        if column_no != column_count-1:
            line_val += str(randint(0,9)) + COLUMN_SEPARATOR
        else:
            line_val += str(randint(0,9))
    return line_val

def create_event_log_file(file_name,line_cnt=10,column_cnt=3):
    file_to_process = open(file_name,"w")
    for line_number in range(line_cnt):
        if line_number != line_cnt-1:
            file_to_process.write(get_random_line_entries(column_cnt)+NEW_LINE_CHAR)
        else:
            file_to_process.write(get_random_line_entries(column_cnt))
    file_to_process.close()

jobs=[]
for file_count_id in range(file_count):
    file_name_with_suffix = file_to_process+str(file_count_id)
    p = Process(target=create_file(file_name_with_suffix,line_count,column_count))
    jobs.append(p)
    p.start()

for curr_job in jobs:
    curr_job.join()
print "process complete"

