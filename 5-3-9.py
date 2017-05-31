# Реализуйте reducer для алгоритма расчета PageRank с помощью Hadoop Streaming.
# Используйте упрощенный алгоритм (без случайных переходов).
# Входные и выходные данные: В качестве ключа идет номер вершины.
# Значение составное: через табуляцию записано значение PageRank (округленное до 3-го знака после запятой)
# и список смежных вершин (через "," в фигурных скобках).

import sys

test_data = ['1	0.067	{}', '1	0.200	{2,4}', '2	0.067	{}', '2	0.100	{}', '2	0.200	{3,5}',
             '3	0.067	{}', '3	0.100	{}', '3	0.200	{4}', '4	0.100	{}', '4	0.200	{}',
             '4	0.200	{5}', '5	0.100	{}', '5	0.200	{}', '5	0.200	{1,2,3}', '6	0.600	{2,3,4}']

(lastKey, lastValue, Pts) = (None, None, '{}')
sumValue = 0
endPts = '{}'

for inp in sys.stdin:
    (key, value, points) = inp.strip().split('\t')
    if lastKey and lastKey != key:
        print(str(lastKey) + '\t' + '{0:.3f}'.format(round(sumValue, 3)) + '\t' + endPts)
        (lastKey, lastValue, Pts) = (key, value, points)
        # sumValue = float(value)
        if points == '{}':
            sumValue = float(value)
        else:
            sumValue = 0
        endPts = points
    else:
        if points == '{}':
            sumValue = sumValue + float(value)
        else:
            endPts = points
        (lastKey, lastValue, Pts) = (key, value, points)
if lastKey:
    print(str(lastKey) + '\t' + '{0:.3f}'.format(round(sumValue, 3)) + '\t' + endPts)
