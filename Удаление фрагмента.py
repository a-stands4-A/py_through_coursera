"""
Дана строка, в которой буква h встречается минимум два раза.
Удалите из этой строки первое и последнее вхождение буквы h, а
также все символы, находящиеся между ними.

Формат ввода

Вводится строка.

Формат вывода

Выведите ответ на задачу.
"""
"""
Тест 1
Входные данные:
In the hole in the ground there lived a hobbit

Вывод программы:
In tobbit



Тест 2
Входные данные:
qwertyhasdfghzxcvb

Вывод программы:
qwertyzxcvb



Тест 3
Входные данные:
asdfghhzxcvb

Вывод программы:
asdfgzxcvb
"""
s = input()

first = s.find("h")
second = len(s) - s[::-1].find("h") - 1

print(s[:first], s[second + 1:], sep='')
