# reducer function for Hadoop Streaming
import sys

(lastKey, sum) = (None, 0)

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    if lastKey and lastKey  != key:
        print(lastKey + '\t' + str(sum))
        (lastKey, sum) = (key, int(value))
    else:
        (lastKey, sum) = (key, sum + int(value))
if lastKey:
    print(lastKey + '\t' + str(sum))
