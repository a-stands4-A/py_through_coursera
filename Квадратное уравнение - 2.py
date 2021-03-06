from math import sqrt
"""
Даны произвольные действительные коэффициенты a, b, c. Решите уравнение
ax²+bx+c=0.

Формат ввода

Вводятся три действительных числа.

Формат вывода

Если данное уравнение не имеет корней, выведите число 0. Если
уравнение имеет один корень, выведите число 1, а затем этот корень.
Если уравнение имеет два корня, выведите число 2, а затем два корня
в порядке возрастания. Если уравнение имеет бесконечно много корней,
выведите число 3.

"""
"""
Тест 1
Входные данные:
1
-1
-2

Вывод программы:
2 -1 2



Тест 2
Входные данные:
1
2
1

Вывод программы:
1 -1



Тест 3
Входные данные:
1
-7.5
3

Вывод программы:
2 0.423966 7.07603
"""
"""
Раце Глеб Сергеевич
2 года назад
"""
a, b, c = float(input()), float(input()), float(input())
d = b**2 - (4 * a * c)
if d < 0 or a == b == 0 and c != 0:
    print(0)
elif a == b == c == 0:
    print(3)
elif d == 0 and a != 0:
    x1 = -b / (2 * a)
    print(1, x1)
elif d > 0 and a != 0:
    x1 = (-b - d**0.5) / (2 * a)
    x2 = (-b + d**0.5) / (2 * a)
    if x1 < x2:
        print(2, x1, x2)
    else:
        print(2, x2, x1)
elif a == 0:
    print(1, -c / b)
