'''Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

*Пример:*

A = 3; B = 5 -> 243 (3⁵)
    A = 2; B = 3 -> 8 
'''

def expon(a, b):
    if b == 1:
        return a
    return a * expon(a,b-1)


def main():
     A = int(input("Enter Number A: "))
     B = int(input("Enter Number B: "))
     print(expon(A, B))

if __name__ == "__main__":
    main()