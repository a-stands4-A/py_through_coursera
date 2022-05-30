"""
В данном списке из n≤10⁵ целых чисел найдите три
числа,произведение которых максимально.

Решение должно иметь сложность O(n),
где n - размер списка. То есть сортировку использовать нельзя.

Выведите три искомых числа в любом порядке.
"""
"""
Тест 1
Входные данные:
3 5 1 7 9 0 9 -3 10

Вывод программы:
10 9 9



Тест 2
Входные данные:
-5 -30000 -12

Вывод программы:
-5 -12 -30000



Тест 3
Входные данные:
1 2 3

Вывод программы:
3 2 1
"""
a = list(map(int, input().split()))
b = a[:]

if len(a) > 3:
    c1 = max(a)
    a.remove(max(a))
    c2 = max(a)
    a.remove(max(a))
    c3 = max(a)
    d1 = min(b)
    b.remove(min(b))
    d2 = min(b)
    b.remove(min(b))
    d3 = min(b)
    if d1 * d2 * c1 > c1 * c2 * c3:
        print(d1, d2, c1)
    else:
        print(c1, c2, c3)
else:
    print(*a)
