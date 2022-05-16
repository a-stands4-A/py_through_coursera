"""
Сложноприводимое условие задачи

"""
"""
Тест 1
Входные данные:
-4
-4

Вывод программы:
NO



Тест 2
Входные данные:
-4
-3

Вывод программы:
NO



Тест 3
Входные данные:
-4
-2

Вывод программы:
NO

"""
"""
Yustina Bubnova
4 месяца назад
"""


def IsPointInArea(x, y):
    s1 = y >= -x and y >= 2 * x + 2 and (x + 1) ** 2 + (y - 1) ** 2 <= 4
    s2 = y <= -x and y <= 2 * x + 2 and (x + 1) ** 2 + (y - 1) ** 2 >= 4
    return s1 or s2


x, y = float(input()), float(input())

if IsPointInArea(x, y):
    print('YES')
else:
    print('NO')
