t = ()  # Кортеж, неизменяемый список

print(type(t))

t = (1,3,5,)
print(type(t))

v=[2,4,6,8]
print(type(v))

print(v)
v =tuple(v)
print(type(v))
print(v)

a, b= 2,4  # множественное присваивание

k,l,m = v

print(k,l,m)

