from random import randint

list_1 = [randint(0, 20) for x in range(20)]

print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
