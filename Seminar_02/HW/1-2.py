import math
import sys
# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

summ = int(input('Enter the summ of X1 and X2: '))
power = int(input('Enter the power of X1 and X2: '))
discr = -power + summ*summ/4
if discr < 0:
    sys.exit("Error input data")
X1 = int(summ/2 + math.sqrt(discr))
X2 = int(summ/2 - math.sqrt(discr))

print(f"Number X1 - {X1}, X2 - {X2}")