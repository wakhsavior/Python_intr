print('{\n"PORT": {')

for i in range(77):
    if i < 48 or i%4 == 0:
        print('\t"Ethernet{}": {}\n\t"alias": "Ethernet{}"\n\t{},'.format(str(i),'{',str(i),'}'))
    # print('{}'.format())

    # ": \n\t"alias": "Ethernet{1}\n\t,
print('}')