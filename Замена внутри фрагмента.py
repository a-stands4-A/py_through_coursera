"""
Дана строка. Замените в этой строке все появления буквы h на букву H,
кроме первого и последнего вхождения.

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
In the Hole in tHe ground tHere lived a hobbit



Тест 2
Входные данные:
qwertyhahsdhfghzxcvb

Вывод программы:
qwertyhaHsdHfghzxcvb



Тест 3
Входные данные:
asdfghhzxcvb

Вывод программы:
asdfghhzxcvb
"""
s = input()
first = s.find("h")
last = s.rfind("h")

if first != last:
    s1 = s[first + 1:last].replace("h", "H")
    s = s[:first + 1] + s1 + s[last:]
print(s)
