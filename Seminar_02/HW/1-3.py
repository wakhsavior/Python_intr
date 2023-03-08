# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input('Enter N: '))
expon = 1
while expon <= N:
    print(expon)
    expon = expon * 2
    
