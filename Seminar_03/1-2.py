# List Shift
###########################

# list_01 = [1,2,3,4,5,6,7,8]
# list_02 = []
# k = int(input("Enter shift: "))
# k = k % len(list_01)
# for i in range(len(list_01)):    
#     list_02.append(list_01[(len(list_01)-k+i)%len(list_01)])
# print(*list_02)

###################################

# list_01 = [1,2,3,4,5,6,7,8]
# k = int(input("Enter shift: "))
# k = k % len(list_01)
# for i in range(1,k+1):
#     last = list_01[len(list_01)-1]
#     for j in range(len(list_01)-1,0,-1):
#         list_01[j] = list_01[j-1]
#     list_01[0] = last
# print(*list_01)

list_01 = [1,2,3,4,5,6,7,8]
k = int(input("Enter shift: "))
k = k % len(list_01)
for i in range(k):
    list_01.insert(0, list_01.pop(-1 ))