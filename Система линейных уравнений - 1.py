"""Даны вещественные числа a, b, c, d, e, f.
Известно, что система линейных уравнений:

ax + by = e

cx + dy = f

имеет ровно одно решение. Выведите два числа x и y,
являющиеся решением этой системы.

Формат ввода

Вводятся шесть чисел a, b, c, d, e, f

- коэффициенты уравнений системы.

Формат вывода

Выведите ответ на задачу.
"""
"""
Тест 1
Входные данные:
1
0
0
1
3
3

Вывод программы:
3 3



Тест 2
Входные данные:
1
2
3
4
-1
-1

Вывод программы:
1 -1



Тест 3
Входные данные:
3
5
4
4
11
12

Вывод программы:
2 1
"""
"""
ELENA CHERNOVA
4 месяца назад
a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())
V = a * d - b * c
x = y = 0
if V != 0:
    x = (e * d - b * f) / V
    y = (a * f - e * c) / V
print(x, y)
"""

a, b, c = float(input()), float(input()), float(input())
d, e, f = float(input()), float(input()), float(input())

V = a * d - b * c
x = (e * d - b * f) / V
y = (a * f - e * c) / V

print(x, y)
