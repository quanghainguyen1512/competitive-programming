# https://www.hackerrank.com/challenges/counting-valleys/problem
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    downs = [s[0]]
    count = 0
    for i, step in enumerate(s[1:]):
        if downs and step != downs[-1]:
            downs.pop()
            if not downs and step == 'U':
                count += 1
        else:
            downs.append(step)

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
