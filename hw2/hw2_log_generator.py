import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process
from collections import defaultdict
import datetime

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


def create_event_log_file(process_id):
    event_log_file = open(str(process_id) + "_" + outfile,"w")
    with open(url_list_file,"r") as urls:
        for url in urls:
            url = url.strip()
            for user_number in range(user_count):
                user_name = "usr" + str(user_number)
                for event_num in range(events_per_user_url):
                    currentTime = str(datetime.datetime.now())
                    #event_log_file.write(url + COLUMN_SEPARATOR + user_name + COLUMN_SEPARATOR + currentTime + NEW_LINE_CHAR)
                    event_log_file.write(currentTime + COLUMN_SEPARATOR + url + COLUMN_SEPARATOR + user_name +NEW_LINE_CHAR)
    event_log_file.close()

jobs=[]
for process_id in range(thread_count):
    p = Process(target=create_event_log_file, args=str(process_id))
    jobs.append(p)
    p.start()

for curr_job in jobs:
    curr_job.join()

print "process complete"

