# все делители числа 284
# 220 = 1 + 2 + 4 + 71 + 142
# все делители числа 220
# 284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110

# N = int(input("Enter number N: "))
# M = int(input("Enter number M: "))

from time import time


def deliteli(N):
    list_N = [1]
    for i in range(2,int(N**0.5)+1):
        if N%i == 0 and i != N//i:
            list_N.append(i)
            list_N.append(N//i)
        elif N%i == 0 and i == N//i:
            list_N.append(i)
    return list_N 
# for k in [10**i for i in range(1,10)]:
start = time()
j = 1
for i in range(3,2000000):
    # print(i, sum(deliteli(i)), deliteli(i))
    first = sum(deliteli(i))
    second = sum(deliteli(first))
    if second == i and second > first:
        print(f"{j}. {first} : {second}")
        j += 1
# print(f"Count {k}: {time() - start}")


# print(deliteli(N))
# print(sum(deliteli(N)))
# print(deliteli(M))
