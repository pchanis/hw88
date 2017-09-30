import argparse
import random
import Queue
import threading
import time
from multiprocessing import Process
from collections import defaultdict
from datetime import datetime, timedelta

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"

prog = "hw2_3"
desc = "Generate test log files of the form <timestamp> <userid> <url>"

parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--outfile','-f',default='events.txt')
parser.add_argument('--user-count','-uc',default=10, type=int)
parser.add_argument('--event-count-user-url','-uuc',default=10, type=int)
parser.add_argument('--url-file','-uf')
parser.add_argument('--thread-count', '-tc', default=4, type=int)

parsed_args = parser.parse_args()
outfile = parsed_args.outfile
user_count = parsed_args.user_count
events_per_user_url = parsed_args.event_count_user_url
url_list_file = parsed_args.url_file
thread_count = parsed_args.thread_count


def create_event_log_file(log_file):
    event_log_file = open(log_file,"w")
    with open(url_list_file,"r") as urls:
        for url in urls:
            url = url.strip()
            for user_number in range(user_count):
                user_name = "usr" + str(user_number)
                for event_num in range(events_per_user_url):
                    hours_offset = random.randrange(-2,3)
                    currenttime = str(datetime.now() + timedelta(hours=hours_offset))
                    event_log_file.write(currenttime + COLUMN_SEPARATOR + url + COLUMN_SEPARATOR + user_name +NEW_LINE_CHAR)
    event_log_file.close()

jobs=[]
for process_id in range(thread_count):
    logfilename = str(process_id) + "_" + outfile
    p = Process(target=create_event_log_file, args=(logfilename,))
    jobs.append(p)
    p.start()

for curr_job in jobs:
    curr_job.join()

print "process complete"

