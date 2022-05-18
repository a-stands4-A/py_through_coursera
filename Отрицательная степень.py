"""
Дано действительное положительное число a и целоe число n.
Вычислите aⁿ. Решение оформите в виде функции power(a, n).
Стандартной функцией возведения в степерь пользоваться нельзя.

Формат ввода

Вводится действительное положительное число a и целоe число n.

Формат вывода

Выведите ответ на задачу.

Примечания

Здесь не нужна рекурсия.

"""
"""
Тест 1
Входные данные:
2
1

Вывод программы:
2



Тест 2
Входные данные:
2
2

Вывод программы:
4



Тест 3
Входные данные:
2
3

Вывод программы:
8
"""
"""
Курбонов Фаррухжон Рауфович
3 месяца назад
"""


def power(a, n):
    if a == 0:
        return 0
    if n == 0:
        return 1
    i = 1
    m = a
    if n > 0:
        while i != n:
            m = m * a
            i += 1
        return m
    if n < 0:
        while i != n:
            m = m / a
            i += -1
        return m


print(power(float(input()), int(input())))
