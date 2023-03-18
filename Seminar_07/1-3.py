

def same_by(characteristic,objects):
    if objects:
        # return len(set([characteristic(i) for i in objects])) ==1
        return len(set(map(characteristic,objects))) == 1
    else:
        return True     



values = [0,2,10,6,12 ]
if same_by(lambda x:x%2, values):
    print('same')
else:
    print('different')