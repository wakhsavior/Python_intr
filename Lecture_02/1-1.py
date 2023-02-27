list_1 = []  # Создает пустой список
list_2 = list() # Пустой список методом
list_3 = [1,2,3,4] # Перечислением значений

print(list_3)
print(*list_3)

for i in list_3:
    print(i)

list_3.append(8)
print(*list_3)
for i in range(10,20,2):
    list_3.append(i)

    print(*list_3)
print(list_3.pop(5))
print(*list_3)

print(list_3.pop())
print(*list_3)

list_3.insert(4,22)
print(*list_3)

print(list_3[-1])
print(*list_3[2:6])

print(list_3[len(list_3)-2:])




