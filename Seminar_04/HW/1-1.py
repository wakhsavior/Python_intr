'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
Затем пользователь вводит сами элементы множеств.

'''

import random
N = int(input("Enter number of element in set 1: "))
M = int(input("Enter number of element in set 2: "))

list_01 = [random.randrange(0,10) for i in range(N) ]
list_02 = [random.randrange(0,10) for i in range(M) ]
set_01 = set(list_01)
set_02 = set(list_02)
set_intersect = set_01.intersection(set_02)

list_sorted = list(set_intersect)
list_sorted.sort()

print(list_01)
print(list_02)
print(list_sorted)