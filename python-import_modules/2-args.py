#!/usr/bin/python3
import sys

arguments = sys.argv[1:]
num_arguments = len(arguments)

if num_arguments == 0:
    print("{} arguments.".format(num_arguments), end='\n')
elif num_arguments == 1:
    print("{} argument:".format(num_arguments), end='\n')
    print("{}: {}".format(num_arguments, sys.argv[1]), end='\n')
else:
    print("{} arguments:".format(num_arguments), end='\n')
    for i in range(num_arguments):
        print("{}: {}".format(i+1, sys.argv[i+1], end='\n'))
