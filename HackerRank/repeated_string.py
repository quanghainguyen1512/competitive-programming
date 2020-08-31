# https://www.hackerrank.com/challenges/repeated-string

import math
import os
import random
import re
import sys


def count_occurences(s):
    count = 0
    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] == 'a':
            count += 1
        if s[j] == 'a':
            count += 1
        i += 1
        j -= 1
    if i == j and s[i] == 'a':
        count += 1
    return count

# Complete the repeatedString function below.
def repeatedString(s, n):
    len_s = len(s)
    n_repeated = n // len_s
    remain = n % len_s
    occ_in_s = count_occurences(s)
    return occ_in_s * n_repeated + count_occurences(s[:remain])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()