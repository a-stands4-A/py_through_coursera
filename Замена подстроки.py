"""
Дана строка. Замените в этой строке все цифры 1 на слово one.

Формат ввода

Вводится строка.

Формат вывода

Выведите ответ на задачу.

"""
"""
Тест 1
Входные данные:
1+1=2

Вывод программы:
one+one=2



Тест 2
Входные данные:
Hello, 2345678990

Вывод программы:
Hello, 2345678990



Тест 3
Входные данные:
1

Вывод программы:
one
"""
s = input()

print(s.replace("1", "one"))
