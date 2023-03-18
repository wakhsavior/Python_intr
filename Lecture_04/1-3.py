lst = [1,2,3,5,8,15,23,38]
itog = []

# for i in lst:
#     if i % 2 == 0:
#         itog.append((i, i** 2 ))


# lst2 = filter(lambda item: item % 2 == 0, lst)

# for i in lst2:
#     a = (i, i * i)
#     itog.append(a)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

itog = select(int,lst)   # Переводим все к целому типу данных 
print(itog)
itog = where(lambda x: x % 2 ==0, itog)    # применяем функцию к каждому элементу, используем как фильтр
print(itog)
itog = select(lambda x: (x, x**2), itog)
print(itog)

# lambda item: item % 2 == 0