class1 = int(input('Учеников в классе 1: '))
class2 = int(input('Учеников в классе 2: '))
class3 = int(input('Учеников в классе 3: '))
parts = class1//2+class1%2 +class2//2+class2%2+class3//2+class3%2
parts = -(-class1//2-class2//2-class3//2)
print(parts)