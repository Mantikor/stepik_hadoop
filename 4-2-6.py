# Напишите reducer, который делает вычитание элементов множества B из множества A.
# На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
import sys

test_data = ['1	A', '2	A', '2	B', '3	B']

(lastKey, lastValue) = (None, None)

tmp = None

for inp in test_data:
    (key, value) = inp.strip().split('\t')
    if not tmp:
        tmp = value
    # print('last key: ', lastKey)
    if lastKey and lastKey != key:
        print('if')
        if lastValue == tmp:
            print(lastKey)
        (lastKey, lastValue) = (key, value)
    else:
        print('else')
        (lastKey, lastValue) = (key, value)
if lastKey:
    # print('last key: ', lastKey)
    if lastValue == tmp:
        print(lastKey)
