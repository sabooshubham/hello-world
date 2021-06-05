#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    altitude = 0
    alt_range = []
    for i in path:
        if i == 'U':
            altitude += 1
        else:
            altitude -= 1
        alt_range.append(altitude)
    count = 0
    for i, alt in enumerate(alt_range):
        if alt == 0 and alt_range[i-1] < 0:
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
