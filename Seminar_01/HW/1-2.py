i = int(input('Enter origami count: '))
if (i%6 ==0):
    print(i//6, i//3*2, i//6)
else:
    print("It isn't possible")