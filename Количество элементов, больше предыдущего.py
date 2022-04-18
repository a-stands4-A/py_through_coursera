"""
Последовательность состоит из натуральных чисел и завершается числом 0.
Определите, сколько элементов этой последовательности больше предыдущего
элемента.

Формат ввода

Вводится последовательность целых чисел, оканчивающаяся числом 0 (само
число 0 в последовательность не входит, а служит как признак ее окончания).

Формат вывода

Выведите ответ на задачу.
"""
N = int(input())
prev = N
spam = 0

while N != 0:
    if N > prev:
        spam += 1
    prev = N
    N = int(input())

print(spam)
