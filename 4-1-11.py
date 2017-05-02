# Реализуйте mapper из фазы 2 задачи Distinct Values v1.
# Mapper принимает на вход строку, содержащую значение и группу, разделенные запятой.

import sys

for inp in sys.stdin:
    (key, value) = inp.strip().split(',')
    print(value + '\t' + '1')
