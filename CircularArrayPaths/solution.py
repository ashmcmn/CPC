#!/bin/python3

import math
import os
import random
import re
import sys


def solve(n, endNodes):
    starts = []
    ends = []

    for i in range(len(endNodes)-1):
        starts.append(endNodes[i])
        ends.append(endNodes[i+1])

    starts.sort()
    ends.sort()

    e = 0
    for s in range(len(starts)):
        if starts[s] <= ends[e]:
            sol = ends[e]
        else:
            e += 1

    print(sol)


if __name__ == '__main__':
    afile = open('input.txt', 'r')

    n = int(afile.readline())

    line = afile.readline()

    endNodes = map(int, line.split())

    solve(n, endNodes)