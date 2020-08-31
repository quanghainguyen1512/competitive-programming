#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    steps = 0
    i = 0
    while i < len(c) - 1:
        if c[i] == 1:
            i -= 1
        steps += 1
        # if i == len(c) - 2:
        #     steps += 1
        i += 2
    return steps

if __name__ == '__main__':
    # fptr = open('./input04.txt', 'w')

    n = 100
    tmp = '0 1 0 0 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 0 0 0 1 0 0 1 0 0 1 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0 1 0 0 0'
    c = list(map(int, tmp.split(' ')))
    result = jumpingOnClouds(c)

    # fptr.write(str(result) + '\n')
    print(result)

    # fptr.close()
