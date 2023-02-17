i = int(input('Введите год '))
if (i%4==0)and (i%400==0)or (i%100!=0):
    print("YES")
else:
    print("NO")

    # (i%4==0)and(i%100!=0)or(i%400==0):