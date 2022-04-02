"""
Даны три стороны треугольника a,b,c. Определите тип треугольника с заданными
сторонами. Выведите одно из четырех слов: rectangular для прямоугольного
треугольника, acute для остроугольного треугольника, obtuse для тупоугольного
треугольника или impossible, если треугольника с такими сторонами не
существует (считаем, что вырожденный треугольник тоже невозможен).

Формат ввода

Вводятся три целых числа.

Формат вывода

Выведите ответ на задачу.
"""
A, B, C = int(input()), int(input()), int(input())
max = 0

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        if A > B:
            if A > C:
                max = A
                if max ** 2 < C ** 2 + B ** 2:
                    print('acute')
                elif max ** 2 == C ** 2 + B ** 2:
                    print('rectangular')
                elif max ** 2 > C ** 2 + B ** 2:
                    print('obtuse')
            else:
                max = C
                if max ** 2 < A ** 2 + B ** 2:
                    print('acute')
                elif max ** 2 == A ** 2 + B ** 2:
                    print('rectangular')
                elif max ** 2 > A ** 2 + B ** 2:
                    print('obtuse')
        elif B > C:
            max = B
            if max ** 2 < C ** 2 + A ** 2:
                print('acute')
            elif max ** 2 == C ** 2 + A ** 2:
                print('rectangular')
            elif max ** 2 > C ** 2 + A ** 2:
                print('obtuse')
        else:
            max = C
            if max ** 2 < A ** 2 + B ** 2:
                print('acute')
            elif max ** 2 == A ** 2 + B ** 2:
                print('rectangular')
            elif max ** 2 > A ** 2 + B ** 2:
                print('obtuse')
    else:
        print('impossible')
else:
    print('impossible')
