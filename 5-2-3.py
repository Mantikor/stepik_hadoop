# Реализуйте алгоритм Дейкстры поиска кратчайшего пути в графе.
# Входные данные: В первой строке указаны два числа: число вершин и число ребер графа.
# Далее идут строки с описанием ребер. Их количество равно числу ребер.
# В каждой строке указаны 3 числа: исходящая вершина, входящая вершина, вес ребра.
# В последней строке указаны 2 номера вершины: начальная и конечная вершина, кратчайший путь между которыми нужно найти.
# Выходные данные: минимальное расстояние между заданными вершинами. Если пути нет, то нужно вернуть -1.

import sys

test_data = ['4 8', '1 2 6', '1 3 2', '1 4 10', '2 4 4', '3 1 5', '3 2 3', '3 4 8', '4 2 1', '1 4']
# test_matrix = [[1000000, 6, 2, 10], [1000000, 1000000, 1000000, 4], [5, 3, 1000000, 8], [1000000, 1, 1000000, 1000000]]

flag = True
matrix = []
test_matrix = []


def DeikstraAlgo(Npin, StartPin, StopPin, matrix):
    valid = [True]*Npin
    weight = [sys.maxsize]*Npin
    weight[StartPin - 1] = 0
    for i in range(Npin):
        min_weight = sys.maxsize + 1
        id_min_weight = -1
        for i in range(len(weight)):
            if valid[i] and weight[i] < min_weight:
                min_weight = weight[i]
                id_min_weight = i
        for i in range(Npin):
            if weight[id_min_weight] + matrix[id_min_weight][i] < weight[i]:
                weight[i] = weight[id_min_weight] + matrix[id_min_weight][i]
        valid[id_min_weight] = False
    if weight[StopPin-1] == sys.maxsize:
        return -1
    else:
        return weight[StopPin-1]

for inp in sys.stdin:
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

for i in range(size):
    line = []
    for j in range(size):
        line.append(sys.maxsize)
    test_matrix.append(line)

for i in range(paths):
    test_matrix[matrix[i][0] - 1][matrix[i][1] - 1] = matrix[i][2]

print(DeikstraAlgo(size, start, finish, test_matrix))