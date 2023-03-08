input_eng = [1,3,3,2,1,4,8,4,1,2,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10]
input_rus = [1,3,1,3,2,1,5,5,1,4,2,2,2,1,1,2,1,1,1,2,10,5,5,5,8,10,10,4,3,8,8,3,3,3]
# print(f"{ord('а')}: ё {ord('ё')})")
# for i in range(34):
#     print(f"{i+1}: {ord('а')+i} : {chr(ord('а')+i)} :{input_rus[i]}")
# print(len(input_eng))
# print(len(input_rus))
string = input("Введите строку русскими буквами: ")
string = string.lower()
summ = 0
for char in string:
    index = ord(char) - ord('а')
    summ += input_rus[index]
    print(f"{char} : {input_rus[index]}")
print(summ)
