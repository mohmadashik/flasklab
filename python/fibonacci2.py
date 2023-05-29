#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#

def fibonacciModified(t1, t2, n):
    t_prev = t1
    t_pres = t2
    t_next = 0
    for i in range(0,n-2):
        if i!= 0:
            t_prev = t_pres
            t_pres = t_next
        t_next = t_prev + t_pres**2
        print(t_next,end='  ')
    print()
    return t_next
    


first_multiple_input = input("give inputs \n").rstrip().split()

t1 = int(first_multiple_input[0])

t2 = int(first_multiple_input[1])

n = int(first_multiple_input[2])

result = fibonacciModified(t1, t2, n)

print(result)
