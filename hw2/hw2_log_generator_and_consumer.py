import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process, Manager
from multiprocessing.managers import BaseManager, DictProxy
from collections import defaultdict
import datetime

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"

prog = "hw2_4"
desc = "Generate test log files of the form <timestamp> <userid> <url>"

parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--logfile','-lf',default='events.txt')
parser.add_argument('--logfile-count', '-lc', default=4, type=int)

parsed_args = parser.parse_args()
logfile = parsed_args.logfile
logfile_count = parsed_args.logfile_count

class MyManager(BaseManager):
    pass

MyManager.register('defaultdict', defaultdict, DictProxy)

mgr = MyManager()
mgr.start()
click_count_by_url_user = mgr.defaultdict(dict)


def process_log(process_id):
    logfile_name = process_id + "_" + logfile
    print "processing log:\t" + logfile_name + NEW_LINE_CHAR
    with open(logfile_name,"r") as events:
        for event in events:
            values = event.split(" ")
            if values[1] not in click_count_by_url_user[values[0]]:
                click_count_by_url_user[values[0]][values[1]] = 1
            else:
                click_count_by_url_user[values[0]][values[1]] += 1

jobs=[]
for process_id in range(logfile_count):
    p = Process(target=process_log, args=str(process_id))
    jobs.append(p)
    p.start()

for curr_job in jobs:
    curr_job.join()

print "log processing complete"
print click_count_by_url_user





