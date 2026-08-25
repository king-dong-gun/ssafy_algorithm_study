n = int(input())
x,y =1,1
a = input().split()

for i in a:
    nx,ny = x,y
    if i =='L':
        ny=y-1
    if i == 'R':
        ny=y+1
    if i == 'U':
        nx=x-1
    if i== 'D':
        nx=x+1
    if nx ==0 or ny ==0:
        continue

    x,y = nx, ny
print(x,y)


'''

5
R R R U D D
        
'''