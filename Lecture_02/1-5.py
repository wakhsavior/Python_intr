list_1 = [i for i in range(1,101)]
print(*list_1)
list_2 = [i for i in range(1,101) if i% 2 ==0]
print(*list_2)

list_3 = [(i,i+1) for i in range(1,101) if i% 2 ==0]
print(*list_3)