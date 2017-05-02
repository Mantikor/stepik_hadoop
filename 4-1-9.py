# Реализуйте mapper из фазы 1 задачи Distinct Values v1. 
# Mapper принимает на вход строку, содержащую значение и через табуляцию список групп, разделенных запятой.

import sys

test_data = ['1	a,b', '2	a,d,e', '1	b', '3	a,b']

for inp in test_data:
    (key, value) = inp.strip().split('\t')
    for letter in value.strip().split(','):
        print(key + ',' + letter + '\t' + '1')
