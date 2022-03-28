"""
Напишите программу, которая считывает два целых числа A и B и выводит
наибольшее значение из них. Числа —  целые от 1 до 1000.

При решении задачи можно пользоваться только целочисленными арифметическими
операциями. Нельзя пользоваться нелинейными конструкциями: ветвлениями,
циклами, функциями.

Формат ввода

Вводятся два числа.

Формат вывода

Выведите ответ на задачу.
"""
"""
Решение с использованием возведения 0 в степень
Литов Максим

Целочисленным делением проверяем, больше ли одно число другого

Например, 20 // 5 = 4, а 5 // 20 = 0

Возведя 0 в степень 0 получим 1. В любой другой степени будет 0.

Умножаем полученное число на одно из чисел, оно либо "останется" преждним,
либо мы его "уберём".

Есть ещё условие, когда числа равны:

a * (0**(a - b))

Так только если числа будут равны друг другу, получим 1 и число "останется"

Питон отказывается возводить 0 в отрицательную степень, что понятно
(делим на ноль) так что просто возводим в 2 разность, нам же 0 нужен, а он
в любой степени 0:

a * (0**((a - b)**2))
"""
a1, a2 = int(input()), int(input())

a1_div = a1 // a2
a2_div = a2 // a1

print(a1 * (0**a2_div) + a2 * (0**a1_div) + a1 * 0**((a1 - a2)**2))
