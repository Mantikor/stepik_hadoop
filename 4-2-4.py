# Напишите reducer, который объединяет элементы из множества A и B. На вход в reducer приходят пары key / value,
# где key - элемент множества, value - маркер множества (A или B)
import sys

(lastKey, lastValue) = (None, None)

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    if lastKey and lastKey  != key:
        print(lastKey)
        (lastKey, lastValue) = (key, value)
    else:
        (lastKey, lastValue) = (key, value)
if lastKey:
    print(lastKey)
