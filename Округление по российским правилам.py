"""
По российский правилам числа округляются до ближайшего целого числа,а  если
дробная часть числа равна 0.5, то число округляется вверх.  Дано
неотрицательное число x, округлите его по этим правилам. Обратите
внимание, что функция round не годится для этой задачи!

Формат ввода

Вводится неотрицательное число.

Формат вывода

Выведите ответ на задачу.

"""
"""
Тест 1
Входные данные:
2.3

Вывод программы:
2



Тест 2
Входные данные:
2.5

Вывод программы:
3



Тест 3
Входные данные:
2.7

Вывод программы:
3
"""
X = float(input())

if X % 1 >= 0.5:
    print(int(X) + 1)
else:
    print(int(X))
