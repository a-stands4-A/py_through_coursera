"""
По данному числу N распечатайте все целые степени двойки, не превосходящие N,
в порядке возрастания.Операцией возведения в степень пользоваться нельзя!

Формат ввода

Вводится натуральное число.

Формат вывода

Выведите ответ на задачу.
"""
N = int(input())
spam = 1
print(1, end=' ')

while spam * 2 <= N and N > 1:
    print(2 * spam, end=' ')
    spam *= 2
