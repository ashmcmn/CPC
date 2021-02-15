#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0] * (n + 1)

    for [a, b, k] in queries:
        arr[a - 1] += k
        arr[b] -= k

    mx = 0
    c = 0
    for x in arr:
        c += x
        mx = max(mx, c)

    return mx


if __name__ == '__main__':
    afile = open('input.txt', 'r')

    nm = afile.readline().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, afile.readline().rstrip().split())))

    result = arrayManipulation(n, queries)

    print(str(result) + '\n')
