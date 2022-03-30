"""
Даны три целых числа. Найдите наибольшее из них (программа должна вывести
ровно одно целое число).

Какое наименьшее число операторов сравнения (>, <, >=, <=) необходимо для
решения этой задачи?

Формат ввода

Вводится три целых числа.

Формат вывода

Выведите ответ на задачу.
"""
A, B, C = int(input()), int(input()), int(input())

if A > B:
    if A > C:
        print(A)
    else:
        print(C)
elif B > C:
    print(B)
else:
    print(C)
