# Реализуйте reducer первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
# Ключ входных данных составной: он содержит слово и номер документа через "#".
# Ключом в выходных данных является слово, а значение состоит из двух элементов, разделенных табуляцией:
# номер документа и tf (сколько раз данное слово встретилось в данном документе).

import sys

test_data = ['aut#1	1', 'aut#1	1', 'aut#1	1', 'aut#1	1', 'aut#2	1', 'aut#2	1', 'bene#2	1',
             'de#2	1', 'mortuis#2	1', 'nihil#1	1', 'nihil#2	1', 'Caesar#1	1']

(lastKey, sum) = (None, 0)

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    if lastKey and (lastKey != key):
        (key1, key2) = lastKey.split('#')
        print(key1 + '\t' + key2 + '\t' + str(sum))
        (lastKey, sum) = (key, int(value))
    else:
        (lastKey, sum) = (key, sum + int(value))
if lastKey:
    (key1, key2) = lastKey.split('#')
    print(key1 + '\t' + key2 + '\t' + str(sum))
