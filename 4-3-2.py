# Реализуйте mapper первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
# Формат входных данных следующий: каждая строка содержит номер документа и строку из него, разделенные ":".
# Ключ выходных данных является составным: он содержит слово документа и его номер, разделенные "#".
# Слово в документе - последовательность символов (букв или цифр), не содержащая пробельных символов и знаков пунктуации.

import sys
import re

test_data = ['1:aut Caesar aut nihil', '1:aut aut', '2:de mortuis aut bene aut nihil',
             '1:a::b', '1:a:::b']

for inp in sys.stdin:
    (key, data) = inp.strip().split(':', 1)
    if data != '':
        words = words = re.split('\W', data)
        for i in words:
            if i != '':
                print(i + '#' + str(key) + '\t' + '1')
