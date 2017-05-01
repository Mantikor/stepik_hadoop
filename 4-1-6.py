# Реализуйте reducer в задаче подсчета среднего времени, проведенного пользователем на странице.
# Mapper передает в reducer данные в виде key / value, где key - адрес страницы, value - число секунд, проведенных пользователем на данной странице.
# Среднее время на выходе приведите к целому числу.

import sys

(lastKey, sum, count) = (None, 0, 0)

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    if lastKey and lastKey != key:
        print(lastKey + '\t' + str(int(sum/count)))
        (lastKey, sum, count) = (key, int(value), 1)
    else:
        (lastKey, sum, count) = (key, sum + int(value), count+1)
if lastKey:
    print(lastKey + '\t' + str(int(sum/count)))
