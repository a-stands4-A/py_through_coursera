"""
По данному числу n вычислите сумму (1 / 1²)+(1 / 2²)+(1 / 3²)+...+(1 / n²).

Формат ввода

Вводится целое положительное число.

Формат вывода

Выведите ответ на задачу.

"""
"""
Тест 1
Входные данные:
3

Вывод программы:
1.36111



Тест 2
Входные данные:
2

Вывод программы:
1.25



Тест 3
Входные данные:
1

Вывод программы:
1
"""
n = int(input())
ssss = 0

while n != 0:
    ssss += 1 / n ** 2
    n -= 1

print(ssss)
