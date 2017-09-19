import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process
import threading
from collections import defaultdict
import datetime

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"
TAB_CHAR = "\t"

prog = "hw2_4"
desc = "Generate test log files of the form <timestamp> <userid> <url>"

parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--logfile','-lf',default='events.txt')
parser.add_argument('--logfile-count', '-lc', default=4, type=int)

parsed_args = parser.parse_args()
logfile = parsed_args.logfile
logfile_count = parsed_args.logfile_count

click_count_by_url_user = defaultdict(dict)
lock = threading.RLock()

def process_log(process_id):
    logfile_name = process_id + "_" + logfile
    with open(logfile_name,"r") as events:
        for event in events:
            event = event.strip(NEW_LINE_CHAR)
            values = event.split(" ")
            url = values[2]
            userid = values[3]
            lock.acquire()
            if userid not in click_count_by_url_user[url]:
                click_count_by_url_user[url][userid] = 1
            else:
                click_count_by_url_user[url][userid] += 1
            lock.release()


def count_unique_urls():
    return len(click_count_by_url_user.keys())


def count_unique_visitors_by_url():
    for key in click_count_by_url_user:
        print key + TAB_CHAR +  str(len(click_count_by_url_user[key]))


def count_unique_userid_clicks_by_url():
    for key in click_count_by_url_user:
        print key
        for user, click_count in click_count_by_url_user[key].items():
            print user + TAB_CHAR + str(click_count)


def query_results():
    #Query 1
    print "Query 1: unique URLs:\t" + str(count_unique_urls())

    #Query 2
    print "Query 2: unique visitors by URL:"
    count_unique_visitors_by_url()

    #Query 3
    print "Query 3: unique user click counts by URL:"
    count_unique_userid_clicks_by_url()


jobs=[]
for process_id in range(logfile_count):
    t = threading.Thread(target=process_log, args=str(process_id))
    jobs.append(t)

for job in jobs:
    job.start()

for curr_job in jobs:
    curr_job.join()

print "log processing complete"

query_results()





