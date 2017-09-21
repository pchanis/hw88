import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process, Pool
import re
import hashlib

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"

prog = "hw2_1a"
desc = "Run multiple cpu-intensive processes"

parser = argparse.ArgumentParser(prog=prog, description=desc)
parser.add_argument('--thread-count','-tc',default=5, type=int)
parser.add_argument('--sleep-time','-st', default=0.001, type=float)

parsed_args = parser.parse_args()
thread_count = parsed_args.thread_count
sleep_time = parsed_args.sleep_time


def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)


def cpu_intensive():
    while 1:
        time.sleep(sleep_time)
        md5("cpu_file.txt")


processes=[]
for thread_count_id in range(thread_count):
    p = Process(target=cpu_intensive)
    p.start()
    processes.append(p)

for curr_proc in processes:
    curr_proc.join()
print "process complete"

