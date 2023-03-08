'''Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
Всего на грядке растет N кустов.Эти кусты обладают разной урожайностью, поэтому ко времени сбора на 
них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена 
система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих 
модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с 
этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может 
собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

'''

import random

N = int(input("Enter the number of bushes in the garden: "))

bush_weight = [random.randrange(5,10) for i in range(N)]

print(bush_weight)
berries_weight = []

for i in range(N):
    weight = bush_weight[i-1] + bush_weight[i] + bush_weight[(i+1)%N]
    berries_weight.append(weight)
print(berries_weight)
maxWeight = max(berries_weight)
bushNum = berries_weight.index(maxWeight)+1

print(f"Max weight of barries {maxWeight}kg is got from 3 bushes is against {bushNum} bush")