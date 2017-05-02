# Реализуйте reducer из фазы 1 задачи Distinct Values v1.
# Reducer принимает на вход данные, созданные mapper из предыдущей шага.
import sys

(lastKey, sum) = (None, 0)

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    if lastKey and lastKey  != key:
        print(lastKey)
        (lastKey, sum) = (key, int(value))
    else:
        (lastKey, sum) = (key, sum + int(value))
if lastKey:
    print(lastKey)
