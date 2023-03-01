# text = 'a a a b c a a d c d d'
text = 'aaabcaadcdd'
print(text)
# dict = {}
# for c in text:
#     if c in dict:
#         print(f'{c}_{dict[c]}', end='')
#     else:
#         print(c, end='')
#     dict[c] = dict.get(c,0)+1
# print()

dict = {}.fromkeys(text,0)
print(dict)
for c in text:
    print(f'{c}_{dict[c]}' if dict[c] else c, end='')
    dict[c] +=1