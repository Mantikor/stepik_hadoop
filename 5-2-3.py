# Реализуйте алгоритм Дейкстры поиска кратчайшего пути в графе.
# Входные данные: В первой строке указаны два числа: число вершин и число ребер графа.
# Далее идут строки с описанием ребер. Их количество равно числу ребер.
# В каждой строке указаны 3 числа: исходящая вершина, входящая вершина, вес ребра.
# В последней строке указаны 2 номера вершины: начальная и конечная вершина, кратчайший путь между которыми нужно найти.
# Выходные данные: минимальное расстояние между заданными вершинами. Если пути нет, то нужно вернуть -1.

import sys

test_data = ['4 8', '1 2 6', '1 3 2', '1 4 10', '2 4 4', '3 1 5', '3 2 3', '3 4 8', '4 2 1', '1 4']

flag = True
matrix = []

for inp in test_data: # sys.stdin:
    [*args] = inp.strip().split(' ')
    for i in range(len(args)):
        args[i] = int(args[i])
    if len(args) == 2 and flag:
        size = args[0]
        paths = args[1]
        flag = False
    elif len(args) == 2 and not flag:
        start = int(args[0])
        finish = int(args[1])
    else:
        matrix.append(args)
    print(args, len(args))

buttons = []
distance = []
checked_v = []

for i in range(size):
    distance.append(sys.maxsize)
    checked_v.append(1)

distance[0] = 0

while True:
    minindex = sys.maxsize
    min = sys.maxsize









    if minindex >= sys.maxsize:
        break

print(size, paths, start, finish)
print(matrix)
print(matrix[0][0], matrix[1][0], matrix[2][0])
print(distance, checked_v)