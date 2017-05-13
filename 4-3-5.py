# Реализуйте reducer второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
# Входные данные: ключ - слово, значение - тройка: номер документа, tf слова в документе и 1 (разделены ';').
# Выходные данные: ключ - пара: слово, номер документа (разделены '#'),
# значение - пара: tf слова в документе, n - количество документов с данным словом (разделены табуляцией).

import sys

test_data = ['aut	1;4;1', 'aut	2;2;1', 'bene	2;1;1', 'de	2;1;1', 'mortuis	2;1;1', 'nihil	1;1;1',
             'nihil	2;1;1', 'Caesar	1;1;1']

test_data1 = ['aut	1;4;1', 'aut	2;2;1', 'aut	3;5;1', 'a 12345;1;1']

(lastKey, sum) = (None, 0)
temp = []

for inp in test_data: # sys.stdin:
    (key, data) = inp.strip().split('\t')
    (num, tf, count) = data.split(';')
    if lastKey and (lastKey != key):
        for i in temp:
            print(i + str(len(temp)))
        temp = []
        temp.append(key + '#' + num + '\t' + tf + '\t')
        (lastKey, sum) = (key, int(count))
    else:
        temp.append(key + '#' + num + '\t' + tf + '\t')
        (lastKey, sum) = (key, sum + int(count))
if lastKey:
    for i in temp:
        print(i + str(len(temp)))
