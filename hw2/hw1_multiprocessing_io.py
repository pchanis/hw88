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
# file_to_process = parsed_args.file
# line_count = parsed_args.line_count
# column_count = parsed_args.column_count
# file_count = parsed_args.file_count
thread_count = parsed_args.thread_count
read_file = parsed_args.read_file

def get_random_line_entries(column_count=3):
    line_val = ""
    for column_no in range(column_count):
        if column_no != column_count-1:
            line_val += str(randint(0,9)) + COLUMN_SEPARATOR
        else:
            line_val += str(randint(0,9))
    return line_val

def create_file(file_name,line_cnt=10,column_cnt=3):
    file_to_process = open(file_name,"w")
    for line_number in range(line_cnt):
        if line_number != line_cnt-1:
            file_to_process.write(get_random_line_entries(column_cnt)+NEW_LINE_CHAR)
        else:
            file_to_process.write(get_random_line_entries(column_cnt))
    file_to_process.close()


def io_intensive():
    while 1:
        with open(read_file, "r") as in_file:
            time.sleep(0.001)
            for line in in_file:
                pass


processes=[]
for thread_count_id in range(thread_count):
    p = Process(target=io_intensive)
    p.start()
    processes.append(p)

for curr_proc in processes:
    curr_proc.join()
print "process complete"

