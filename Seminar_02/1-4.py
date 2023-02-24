import sys
number = int(input('Enter count: '))

light = sys.maxsize
heavy = 0
for i in range(number):
    weight = int(input("Enter Weight: "))
    if (weight >= heavy):
        heavy = weight
    if (weight <= light):
        light = weight
print(f"{light} - {heavy}")