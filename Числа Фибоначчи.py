"""
Последовательность Фибоначчи определяется так:

F[0] = 0, F[1] = 1, ..., F[n] = F[n-1] + F[n-2].

По данному числу n определите n-е число Фибоначчи F[n].

Формат ввода

Вводится натуральное число n.

Формат вывода

Выведите ответ на задачу.
"""
"""
by Мухин Иван Владимирович
9 месяцев назад
"""
n = int(input())

f1, f2 = 0, 1

while n:
    f1, f2 = f2, f1 + f2
    n -= 1

print(f1)
