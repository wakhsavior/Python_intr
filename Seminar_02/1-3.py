# наибольшее количество дней когда среднесуточная температура была больше 0

days = int(input('Enter days count: '))

result = 0
count = 0
for i in range(days):
    temp = int(input("Enter temperature: "))
    if temp >= 0:
        count += 1
    else:
        count =0
    if count > result:
        result = count
print(f"The count of days is {result}")