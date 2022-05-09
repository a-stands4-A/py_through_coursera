"""
Дана строка, в которой буква h встречается как минимум два раза.
Выведите измененную строку: повторите последовательность символов,
заключенную между первым и последним появлением буквы h два раза
(сами буквы h не входят в повторяемый фрагмент, т. е. их повторять не надо).

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
In the hole in the ground there lived a e hole in the
ground there lived a hobbit



Тест 2
Входные данные:
qwertyhasdfghzxcvb

Вывод программы:
qwertyhasdfgasdfghzxcvb



Тест 3
Входные данные:
asdfghhzxcvb

Вывод программы:
asdfghhzxcvb
# """
s = input()

first = s.find("h")
second = len(s) - s[::-1].find("h") - 1

s2 = s[:second] + s[first + 1:second] + s[second:]

print(s2)
