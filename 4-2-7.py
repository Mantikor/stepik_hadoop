# Напишите reducer, который реализует симметричную разность множеств A и B (т.е. оставляет только те элементы,
# которые есть только в одном из множеств). 
# На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)
# решение жестяк, но я устал )))

import sys

test_data = ['1	A',
             '2	A',
             '3	A',
             '4	B',
             '5	B',
             '6	B',
             '7	A',
             '8	A',
             '8	B',
             '10	B',
             '11	A',
             '11	B',
             '12	B',
             '13	B',]

import sys

arr = [[None, None], [None, None], [None, None]]

endof = [0, 1, 2]

for inp in sys.stdin:
    (key, value) = inp.strip().split('\t')
    if arr[0][0]:
        if arr[0][0] == arr[1][0]:
            arr[0][0] = None
            arr[0][1] = None
            arr[1][0] = arr[2][0]
            arr[1][1] = arr[2][1]
        else:
            print(arr[0][0])
            arr[0][0] = arr[1][0]
            arr[0][1] = arr[1][1]
            arr[1][0] = arr[2][0]
            arr[1][1] = arr[2][1]
    else:
        arr[0][0] = arr[1][0]
        arr[0][1] = arr[1][1]
        arr[1][0] = arr[2][0]
        arr[1][1] = arr[2][1]
    arr[2][0] = key
    arr[2][1] = value
for i in endof:
    if arr[0][0]:
        if arr[0][0] == arr[1][0]:
            arr[0][0] = None
            arr[0][1] = None
            arr[1][0] = arr[2][0]
            arr[1][1] = arr[2][1]
        else:
            print(arr[0][0])
            arr[0][0] = arr[1][0]
            arr[0][1] = arr[1][1]
            arr[1][0] = arr[2][0]
            arr[1][1] = arr[2][1]
    else:
        arr[0][0] = arr[1][0]
        arr[0][1] = arr[1][1]
        arr[1][0] = arr[2][0]
        arr[1][1] = arr[2][1]
    arr[2][0] = None
    arr[2][1] = None

