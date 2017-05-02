# Реализуйте reducer из задачи Distinct Values v2.
# Reducer принимает на вход строки, каждая из которых состоит из разделенных табуляцией значения и названия группы.

import sys

test_data = ['1	a', '1	b', '1	b', '2	a', '2	d', '2	e', '3	a', '3	b']

def combiner(tmp_lst):
    (lastKey, sum) = (None, 0)
    tmp_lst.sort()
    for inp in tmp_lst:
        (key, value) = inp.strip().split(',')
        if lastKey and lastKey != key:
            print(lastKey + '\t' + str(sum))
            (lastKey, sum) = (key, 1)
        else:
            (lastKey, sum) = (key, sum + 1)
    if lastKey:
        print(lastKey + '\t' + str(sum))

temp_list = set()
for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    temp_list.add(value+','+key)
temp_list = list(temp_list)
combiner(temp_list)
