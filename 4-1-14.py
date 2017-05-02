# Реализуйте mapper для задачи Cross-Correlation, который для каждого кортежа создает все пары элементов,
# входящих в него.
# Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
# Mapper пишет данные в виде key / value, где key - пара объектов, разделенных запятой, value - единица.

import sys

test_data = ['a b', 'a b a c']

for inp in sys.stdin:
    data = inp.strip().split(' ')
    for i in data:
        for j in data:
            if i != j:
                print(i+','+j+'\t'+'1')
