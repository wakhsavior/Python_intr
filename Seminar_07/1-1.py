# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета.

orbits = [(1,3),(2.5,10),(7,2),(6,6),(4,3)]



def find_farthest_orbit(lst):
    s = { i[0] * i[1]: i  for i in lst if i[0] != i[1]}
    print(s.items())
    return max(s.items())[1]

# orbits = [tuple(map(int,input().split())) for i in range(int(input("qnt:")))]    

print(*find_farthest_orbit(orbits))