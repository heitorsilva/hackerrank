#!/bin/python3

import math
import os
import random
import re
import sys

from functools import reduce
from itertools import groupby

def sockMerchant(n, ar):
    ar.sort()
    ar = list(map(lambda q: q / 2 if q % 2 == 0 else (q-1) / 2, [len(list(g)) for k, g in groupby(ar)]))
    total = reduce(lambda x, y: x + y, ar)

    return int(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
