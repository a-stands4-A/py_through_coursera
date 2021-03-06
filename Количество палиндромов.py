"""
Назовем число палиндромом, если оно не меняется при перестановке его
цифр в обратном порядке. Напишите программу, которая по заданному числу
K выводит количество натуральных палиндромов, не превосходящих K.

Формат ввода

Задано единственное число K (1≤K≤100000).

Формат вывода

Необходимо вывести количество натуральных палиндромов, не превосходящих K.
"""
K = int(input())
amount = 0
spam = K
rev = '0'

while spam != 0:
    rev = str(K % 10)
    K //= 10
    while K:
        rev += str(K % 10)
        K //= 10
    if rev == str(spam):
        amount += 1
    spam -= 1
    K = spam

print(amount)
