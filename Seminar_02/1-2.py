# Вычислить номер числа Фибоначчи
#   0 1 2 3 4 5 6 7  8  9  10 11 12  13  14  15  16
#   0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987

n = int(input('Enter Number: '))

i = 1
a = 0
b = 1

while n >= b:
    if n == b:
        print(f"Count Fibonachi {n} = {i}")
        break
    a, b = b, a + b
    # b = a + b
    # a = b - a
    i += 1
else:
    print(-1)
