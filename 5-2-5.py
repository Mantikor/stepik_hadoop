# Реализуйте mapper в задаче поиска кратчайшего пути с помощью Hadoop Streaming.
# Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:
# Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
# Список исходящих вершин (через "," в фигурных скобках)

import sys

test_data = ['1	0	{2,3,4}', '2	1	{5,6}', '3	1	{}', '4	1	{7,8}', '5	INF	{9,10}', '6	INF	{}',
             '7	INF	{}', '8	INF	{}', '9	INF	{}', '10	INF	{}']

for inp in sys.stdin:
    (key, value, points) = inp.strip().split('\t')
    print(key + '\t' + value + '\t' + points)
    points = list(str(points).lstrip('{').rstrip('}').split(','))
    # print(points, len(points))
    if value == 'INF':
        pass
    else:
        value = str(int(value)+1)
    if points != ['']:
        for i in points:
            print(str(i) + '\t' + value + '\t' + '{}')
