"""
В этой задаче необходимо проверить, делится ли число A на число B нацело.
Использовать можно только арифметические операции, использование любых
видов ветвлений, функций и т.п. запрещено.

Формат ввода

Вводятся два натуральных числа A и B.

Формат вывода

Выведите "YES", если A кратно B и "NO" в противном случае
"""
a1, a2 = int(input()), int(input())

a1_div = a1 % a2
a2_div = 0 ** a1_div

print(a2_div * "YES" + (1 - a2_div) * "NO")
