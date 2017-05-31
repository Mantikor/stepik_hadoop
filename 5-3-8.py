# Реализуйте mapper для алгоритма расчета PageRank с помощью Hadoop Streaming.
# Входные и выходные данные: В качестве ключа идет номер вершины.
# Значение составное: через табуляцию записано значение PageRank (округленное до 3-го знака после запятой)
# и список смежных вершин (через "," в фигурных скобках).

import sys

test_data = ['1	0.200	{2,4}', '2	0.200	{3,5}', '3	0.200	{4}', '4	0.200	{5}', '5	0.200	{1,2,3}']

for inp in sys.stdin:
    (key, value, points) = inp.strip().split('\t')
    print(key + '\t' + value + '\t' + points)
    points = list(str(points).lstrip('{').rstrip('}').split(','))
    # print(points, len(points))
    if len(points) > 0:
        value = float(value) / len(points)
        for i in points:
            # print(i + '\t' + str(round(value, 3)) + '\t' + '{}')
            print(i + '\t' + '{0:.3f}'.format(round(value, 3)) + '\t' + '{}')
