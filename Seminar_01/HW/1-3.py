i = int(input('Enter Number: '))
sum1 = 0
sum2 = 0
while i//1000 != 0:
    sum1 = sum1 + i%10
    i= i//10
while i != 0:
    sum2 = sum2 + i%10
    i= i//10
if sum1==sum2:
    print("Yes")
else:
    print("No")