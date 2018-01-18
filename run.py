#!/usr/bin/python

import sys, subprocess, os

if len(sys.argv) != 2:
    print("Usage: ./run.py <number>")
    sys.exit(1)

problem_num = int(sys.argv[1])
problem_set = problem_num // 25

set_start = problem_set * 25 + 1
set_end = (problem_set + 1) * 25

directory = "p%03d-%03d" % (set_start, set_end)
filepath = "p" + str(problem_num) + ".py"

os.chdir(directory)
subprocess.call("python3 " + filepath, shell=True)
os.chdir("../")
