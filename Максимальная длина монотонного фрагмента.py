"""
Дана последовательность натуральных чисел, завершающаяся числом 0.
Определите наибольшую длину монотонного фрагмента последовательности
(то есть такого фрагмента, где все элементы либо больше предыдущего,
либо меньше).

Формат ввода

Вводится последовательность целых чисел, оканчивающаяся числом 0 (само число 0
в последовательность не входит, а служит как признак ее окончания).

Формат вывода

Выведите ответ на задачу.
"""
inp = int(input())
prev = inp
amountBig = 0
amountSml = 0
strickBig = 1
strickSml = 1

while inp:
    if inp > prev:
        amountBig += 1
        amountSml = 1
        prev = inp
        if amountBig > strickBig:
            strickBig = amountBig
    elif inp < prev:
        amountSml += 1
        amountBig = 1
        prev = inp
        if amountSml > strickSml:
            strickSml = amountSml
    else:
        amountBig = 1
        amountSml = 1
    inp = int(input())

if strickBig > strickSml:
    print(strickBig)
else:
    print(strickSml)
