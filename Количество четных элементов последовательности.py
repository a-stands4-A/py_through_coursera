"""
Определите количество четных элементов в последовательности,
завершающейся числом 0.

Формат ввода

Вводится последовательность целых чисел, оканчивающаяся числом 0
(само число 0 в последовательность не входит, а служит как признак
ее окончания).

Формат вывода

Выведите ответ на задачу.
"""
N = int(input())
spam = 0

while N != 0:
    if N % 2 == 0:
        spam += 1
    N = int(input())

print(spam)
