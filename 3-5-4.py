# mapper function for Hadoop Streaming
import sys


for inp in sys.stdin:
    for wrd in inp.strip().split(' '):
        if wrd:
            print(wrd + '\t1')
