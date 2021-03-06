"""
В списке все элементы попарно различны.
Поменяйте местами минимальный и максимальный элемент
этого списка.

Формат ввода

Вводится список целых чисел. Все числа списка
находятся на одной строке.

Формат вывода

Выведите ответ на задачу.

"""
"""
Тест 1
Входные данные:
3 4 5 2 1

Вывод программы:
3 4 1 2 5



Тест 2
Входные данные:
1 5 4 3 2

Вывод программы:
5 1 4 3 2



Тест 3
Входные данные:
-30000 30000

Вывод программы:
30000 -30000
"""
a = list(map(int, input().split()))

Min = a.index(min(a))  # индекс наименьшего элемента
Max = a.index(max(a))  # индекс наибольшего элемента
a[Min], a[Max] = a[Max], a[Min]

print(*a)
