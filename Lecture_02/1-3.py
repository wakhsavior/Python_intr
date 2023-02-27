dict = {}
dict['q'] = 'qwerty'

print(dict)
print(dict['q'])

dict['a'] = 'asdfgh'
dict[23] = 33432
dict['alpha'] = 'betta'

print(dict)
print(dict['q'])
print(dict['a'])

for item in dict:
    print(item) 
    print('{}: {}'.format(item, dict[item]))
for (k,v) in dict.items():
    print(k,v)