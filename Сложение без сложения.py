"""
Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух
целых неотрицательных чисел. Из всех арифметических операций
допускаются только +1 и -1. Также нельзя использовать циклы.

Формат ввода

Вводятся два удовлетворяющих условию задачи числа. Числа не превышают 900.

Формат вывода

Выведите ответ на задачу.

"""
"""
Тест 1
Входные данные:
2
2

Вывод программы:
4



Тест 2
Входные данные:
123
456

Вывод программы:
579



Тест 3
Входные данные:
179
0

Вывод программы:
179
"""


def sum(a, b):
    if a == 0:
        return b
    else:
        b += 1
        a -= 1
        return sum(a, b)


print(sum(int(input()), int(input())))
