data = ['12', '44', '325', '543', '234', '435', '55', '43', '65', '342', '343', '65']

# file = open('myfile.txt', 'a')
# file.writelines(data)
# file.close()

# with open('myfile.txt', 'w') as file:
#     file.write('line 1\n')
#     file.write('line 2\n')
# print(1)

path = 'myfile.txt'
file = open(path, 'r')
for line in file:
    print(line)
file.close()
