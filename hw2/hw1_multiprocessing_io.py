import argparse
from random import randint
import Queue
import threading
import time
from multiprocessing import Process, Pool
import re
import os

COLUMN_SEPARATOR = " "
NEW_LINE_CHAR = "\n"

prog = "hw2_1a"
desc = "Run multiple cpu-intensive processes"

parser = argparse.ArgumentParser(prog=prog, description=desc)

# parser.add_argument('--file','-f',default='output.txt')
# parser.add_argument('--line-count','-l',default=10, type=int)
# parser.add_argument('--column-count','-c',default=3, type=int)
# parser.add_argument('--file-count','-fc',default=5, type=int)
parser.add_argument('--thread-count','-tc',default=5, type=int)
parser.add_argument('--read_file','-rf', default="file.txt")

parsed_args = parser.parse_args()
thread_count = parsed_args.thread_count
read_file = parsed_args.read_file


def io_intensive(proc_id):
    while 1:
        with open(read_file, "r") as in_file, open(read_file + "copy" + str(proc_id),"w") as write_file:
            time.sleep(0.001)
            for line in in_file:
                write_file.write(line)



processes=[]
for thread_count_id in range(thread_count):
    p = Process(target=io_intensive, args=(thread_count,))
    p.start()
    processes.append(p)

for curr_proc in processes:
    curr_proc.join()
print "process complete"

