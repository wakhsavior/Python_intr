# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет,  которые нужно перевернуть.

n = int(input('Enter the number of coins: '))
count = 0
for i in range(n):
    head = 10
    while (head!=0) and (head !=1):
        head = int(input('Input head (head - 1, tail - 0): '))
    count += head
if (n - count)>count:
    count
else:
    count = n - count
print(f"The count of coins is needed to rotate: {count}")