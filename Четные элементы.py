"""
Выведите все четные элементы списка.

Формат ввода

Вводится список чисел. Все числа списка находятся на одной строке.

Формат вывода

Выведите ответ на задачу.

"""
"""
Тест 1
Входные данные:
1 2 2 3 3 3 4

Вывод программы:
2 2 4



Тест 2
Входные данные:
1 2 3 4 5

Вывод программы:
2 4



Тест 3
Входные данные:
2 4 6 8

Вывод программы:
2 4 6 8
"""
a = list(map(int, input().split()))

for i in a:
    if i % 2 == 0:
        print(i, end=' ')
