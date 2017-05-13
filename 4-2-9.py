# Напишите reducer, реализующий объединение двух файлов (Join) по id пользователя.
# Первый файл содержит 2 поля через табуляцию: id пользователя и запрос в поисковой системе.
# Второй файл содержит id пользователя и URL, на который перешел пользователь в поисковой системе.
# Mapper передает данные в reducer в виде key / value, где key - id пользователя, value состоит из 2 частей:
# маркер файла-источника (query или url) и запрос или URL.
# Каждая строка на выходе reducer должна содержать 3 поля, разделенных табуляцией: id пользователя, запрос, URL.

import sys

test_data = ['user1	query:гугл', 'user1	url:google.ru', 'user2	query:стэпик',
             'user2	query:стэпик курсы', 'user2	url:stepic.org', 'user2	url:stepic.org/explore/courses',
             'user3	query:вконтакте']

query = []
url = []
for inp in sys.stdin:
    (user, data) = inp.strip().split('\t')
    (key, value) = data.split(':')
    if key == 'query':
        query.append([user, value])
    elif key == 'url':
        url.append([user, value])
for i in query:
    for j in url:
        if i[0] == j[0]:
            print(i[0] + '\t' + i[1] + '\t' + j[1])
