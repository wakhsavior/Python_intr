input = [0,-1,5,2,3,3,5,2,5,8,-2,-4,4,3,5,6]
print(len([1 for i in range(len(input)-1) if input[i+1]>input[i]]))

print(sum([input[i] > input[i-1] for i in range(1,len(input))]))