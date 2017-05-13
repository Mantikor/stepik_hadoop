# Дан файл с логами переходов пользователей. Каждая строка состоит из 3 полей: время перехода (unix timestamp),
# ID пользователя, URL, на который перешел пользователь.
# Напишите mapper с помощью Hadoop Streaming, печатающий URL из каждой строки.
import sys

test_data = ['1448713968	user2	https://ru.wikipedia.org/', '1448764519	user10	https://stepic.org/',
             '1448713968	user5	http://google.com/', '1448773411	user10	https://stepic.org/explore/courses',
             '1448709864	user3	http://vk.com/']

for inp in sys.stdin:
    (one, two, three) = inp.strip().split('\t')
    print(three)
