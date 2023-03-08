# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random


def main():
    N = int(input("Number of element in List: "))
    a = int(input("Edge-1 of diapazone: "))
    b = int(input("Edge-2 of diapazone: "))
    if a > b:
        a,b = b,a
    list_01 = [random.randint(1,20) for i in range(N)]
    count = 0
    print(list_01)
    print(f"{a} : {b}")
    for i in range(len(list_01)):
        if a <= list_01[i] <= b:
            print(i)    
    print (count)
    

if __name__ == "__main__":
    main()