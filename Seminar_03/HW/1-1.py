import random

N = int(input("Enter array size: "))
list_01 = [random.randrange(0,10) for i in range(N)] 
print(list_01)
num = int(input("Enter number: "))
print(len([1 for i in range(N) if num == list_01[i]]))
