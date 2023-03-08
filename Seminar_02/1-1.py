# Вычислить факториал числа

n = int(input('Enter Number: '))
factorial = 1
i=2
while(i<=n):
    factorial *= i
    i+=1
print(f"{n}! = {factorial}")
