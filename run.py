#!/usr/bin/python

import sys, os

if len(sys.argv) != 2:
    print("Usage: ./run.py <number>")
    sys.exit(1)

problem_num = int(sys.argv[1])
problem_set = problem_num // 25

set_start = problem_set * 25 + 1
set_end = (problem_set + 1) * 25

directory = "p%03d-%03d" % (set_start, set_end)
filepath = directory + "/p" + str(problem_num) + ".py"

os.system("python3 " + filepath)
