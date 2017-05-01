# Реализуйте Combiner в задаче подсчета среднего времени, проведенного пользователем на странице.
# Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара чисел, разделенных ";".
# Первое - число секунд, проведенных пользователем на данной странице, второе равно 1.

import sys

(lastKey, sum, sum2) = (None, 0, 0)

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    (value, value2) = value.split(';')
    if lastKey and lastKey  != key:
        print(lastKey + '\t' + str(sum)+';'+str(sum2))
        (lastKey, sum, sum2) = (key, int(value), int(value2))
    else:
        (lastKey, sum, sum2) = (key, sum + int(value), sum2+1)
if lastKey:
    print(lastKey + '\t' + str(sum)+';'+str(sum2))
