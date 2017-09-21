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

prog = "hw2_1b_multiprocessing_io_intensive"
desc = "Generate multiprocess io intensive load by reading and copy a file"

parser = argparse.ArgumentParser(prog=prog, description=desc)

parser.add_argument('--process-count','-pc',default=5, type=int)
parser.add_argument('--read_file','-rf', default="file.txt")

parsed_args = parser.parse_args()
process_count = parsed_args.process_count
read_file = parsed_args.read_file


def io_intensive(proc_id):
    rf = open(read_file,"r")
    wf = open(read_file+"copy"+str(proc_id),"w")
    while 1:
        time.sleep(0.001)
        for line in rf.readline():
            wf.write(line)

processes=[]
for process_count_id in range(process_count):
    p = Process(target=io_intensive, args=(process_count_id,))
    p.start()
    processes.append(p)

for curr_proc in processes:
    curr_proc.join()
print "process complete"

