import random
import sys

N = int(input("Enter array size: "))
list_01 = [random.randrange(0,10) for i in range(N)] 
print(list_01)
num = int(input("Enter number: "))
diff = sys.maxsize
result = sys.maxsize
for i in range(N):
    if (abs(list_01[i] - num) < diff):
        diff = abs(list_01[i] - num)
        result = list_01[i]
        # print("{} : {}".format(result,diff))
print(result)