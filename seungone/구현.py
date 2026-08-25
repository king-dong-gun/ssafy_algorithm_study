a=(1,2,3,4,5,6,7,8)
b=('a','b','c','d','e','f','g','h')

n = input()
r1 = int(n[1])
r2 = ord(n[0])-ord('a')+1

steps = [(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
count =0
for c,d in steps:
    dx=r2+c
    dy=r1+d
    if 0< dx <=8  and 0<dy<=8:
        count+=1

print(count)



