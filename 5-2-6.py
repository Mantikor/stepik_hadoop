# Реализуйте reducer в задаче поиска кратчайшего пути с помощью Hadoop Streaming.
# Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:
# Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
# Список исходящих вершин (через "," в фигурных скобках).

import sys

test_data = ['1	0	{2,3,4}', '10	INF	{}', '10	INF	{}', '2	1	{}', '2	1	{5,6}', '3	1	{}', '3	1	{}',
             '4	1	{}', '4	1	{7,8}', '5	2	{}', '5	INF	{9,10}', '6	2	{}', '6	INF	{}', '7	2	{}',
             '7	INF	{}', '8	2	{}', '8	INF	{}', '9	INF	{}', '9	INF	{}']

(lastKey, lastValue, Pts) = (None, None, '{}')

for inp in test_data: # sys.stdin:
    (key, value, points) = inp.strip().split('\t')
    # print(key + '\t' + value + '\t' + points)
    # points = list(str(points).lstrip('{').rstrip('}').split(','))
    # print(points, len(points))
    if lastKey and (lastKey != key):
        # print(lastKey)
        # (lastKey, lastValue, Pts) = (key, value, points)
        print(str(lastKey) + '\t' + str(lastValue) + '\t' + Pts)
        (lastKey, lastValue, Pts) = (key, value, points)
    else:
        if points != '{}':
            if lastKey:
                (lastKey, Pts) = (key, points)
                if key != 'INF' and int(key)<int(lastKey):
                    lastKey = key
            else:
                (lastKey, lastValue, Pts) = (key, value, points)
        else:
            if key != 'INF' and int(key)<int(lastKey):
                lastKey = key
        # print(str(lastKey) + '\t' + str(lastValue) + '\t' + Pts)
        # if lastValue != None and value:
        #     print(lastKey)
        # (lastKey, lastValue) = (key, value)
if lastKey:
    print(str(lastKey) + '\t' + str(lastValue) + '\t' + Pts)

