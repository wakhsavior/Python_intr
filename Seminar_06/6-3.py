from time import time
from random import choices


list_01 = [1,2,3,4,2,3,8,4,3,5,6,5,3,8]
# list_01 = choices(range(3000), k=2000)

# list_02 = list(set(list_01))
# print(list_02)
# count = 0
# for i in range(len(list_02)):
#     count += list_01.count(list_02[i])//2
# print(count) 


start = time()

dict_list = {}.fromkeys(list_01,0)
print(dict_list)
for i in list_01:
    dict_list[i] += 1
print(time() - start)

print(dict_list)
print([i//2 for i in dict_list.values() if not i%2 ])

