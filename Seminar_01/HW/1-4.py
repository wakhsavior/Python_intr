n = int(input('Enter chocolate length: '))
m = int(input('Enter chocolate width: '))
k = int(input('Enter number of  slices: '))

if ((k%n==0) or (k%m==0)) and (m*n!=k):
    print("Yes")
else:
    print("No")
