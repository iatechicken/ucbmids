#!/usr/bin/env python
"""
This script reads word counts from STDIN and aggregates
the counts for any duplicated words.

INPUT & OUTPUT FORMAT:
    word \t count
USAGE (standalone):
    python aggregateCounts_v2.py < yourCountsFile.txt

Instructions:
    For Q7 - Your solution should not use a dictionary or store anything
             other than a single total count - just print them as soon as
             you've added them. HINT: you've modified the framework script
             to ensure that the input is alphabetized; how can you
             use that to your advantage?
"""

# imports
import sys
from itertools import groupby
from operator import itemgetter

################# YOUR CODE HERE #################
def data_read(file):
    for line in file:
        yield line.split()

data = data_read(sys.stdin)

for word, group in groupby(data, itemgetter(0)):
    total_count  = sum(int(count) for word, count in group )
    print("{}\t{}".format(word,total_count))

################ (END) YOUR CODE #################
