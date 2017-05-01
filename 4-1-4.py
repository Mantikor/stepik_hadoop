# mapper v1 function for Hadoop Streaming
import sys

def combiner(tmp_lst):
    (lastKey, sum) = (None, 0)
    tmp_lst.sort()
    for inp in tmp_lst:
        key = inp[0]
        value = inp[1]
        if lastKey and lastKey != key:
            print(lastKey + '\t' + str(sum))
            (lastKey, sum) = (key, int(value))
        else:
            (lastKey, sum) = (key, sum + int(value))
    if lastKey:
        print(lastKey + '\t' + str(sum))

for inp in sys.stdin:
    temp_list = []
    for wrd in inp.strip().split(' '):
        if wrd:
            temp_list.append([wrd, 1])
    combiner(temp_list)

