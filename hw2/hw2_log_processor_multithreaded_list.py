import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process
import threading
from collections import defaultdict, Counter
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

list_dicts = []

def process_log(process_id, process_dict):
    logfile_name = process_id + "_" + logfile
    with open(logfile_name,"r") as events:
        for event in events:
            event = event.strip(NEW_LINE_CHAR)
            values = event.split(" ")
            url = values[2]
            userid = values[3]
            if userid not in process_dict[url]:
                process_dict[url][userid] = 1
            else:
                process_dict[url][userid] += 1


def count_unique_urls():
    urls = []
    for d in list_dicts:
        urls.extend(list(d))
    unique_urls = set(urls)
    return len(unique_urls)


def count_unique_visitors_by_url():
    users_by_url = defaultdict(list)
    for d in list_dicts:
        for k in d.keys():
            for u in d[k]:
                users_by_url[k].append(u)
    for k in users_by_url.keys():
        users_by_url[k] = set(users_by_url[k])
        print k + TAB_CHAR + str(len(users_by_url[k]))


def count_unique_userid_clicks_by_url():
    count_unique_clicks_by_user_by_url = defaultdict(dict)
    for d in list_dicts:
        for k in d.keys():
            for u,v in d[k].items():
                if u not in count_unique_clicks_by_user_by_url[k]:
                    count_unique_clicks_by_user_by_url[k][u] = v
                else:
                    count_unique_clicks_by_user_by_url[k][u] += v
    for k in count_unique_clicks_by_user_by_url.keys():
         print k + ":"
         for u,v in count_unique_clicks_by_user_by_url[k].items():
             print u + TAB_CHAR + str(v)


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
    list_dicts.append(defaultdict(dict))
    t = threading.Thread(target=process_log, args=(str(process_id), list_dicts[process_id]))
    jobs.append(t)

for job in jobs:
    job.start()

for curr_job in jobs:
    curr_job.join()

print "log processing complete"
#print list_dicts
#print len(list_dicts)
query_results()





