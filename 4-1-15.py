# Реализуйте mapper для задачи Cross-Correlation, который для каждого объекта из кортежа создает stripe.
# Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
# Mapper пишет данные в виде key / value, где key - объект, value - соответствующий stripe (пример: a:1,b:2,c:3)

import sys

test_data = ['a b', 'a b a c']

for inp in sys.stdin:
    data = inp.strip().split(' ')
    for i in data:
        base = i+'\t'
        stripe = {}
        extend = ''
        for j in data:
            if i != j:
                if j in stripe:
                    stripe[j] = stripe[j]+1
                else:
                    stripe[j] = 1
        for j in stripe:
            extend = extend+str(j)+':'+str(stripe[j])+','
        print(base+extend[:-1])
