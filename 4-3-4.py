# Реализуйте mapper ﻿второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
# Во входных данных ключом является слово, а значение состоит из номера документа и tf, разделенных табуляцией.
# Значение в выходных данных - это тройка: номер документа, tf и единица, разделенные ";".

import sys

test_data = ['aut	1	4', 'aut	2	2', 'bene	2	1',
             'de 2   1', 'mortuis	2	1', 'nihil	1	1',
             'nihil	2	1', 'Caesar	1	1']

for inp in sys.stdin:
    (key, value, data) = inp.strip().split('\t')
    print(key + '\t' + value + ';' + data + ';' + '1')
