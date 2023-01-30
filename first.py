l=[1,2,4,8,16,32,64]
x=5
i=0
while i<len(l):
    if 2**x==l[i]:
        print('at index',i)
        break
    else: 
        i=i+1
else: print(x, 'non found')