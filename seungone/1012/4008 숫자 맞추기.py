#4008 숫자 맞추기 
def perm(dep,result):
    global max_v,min_v
    if dep==n:
        max_v=max(max_v,result)
        min_v=min(min_v,result)
        return
    for i in range(4):
        if arr[i]>0:
            arr[i]-=1
            if i==0:
                perm(dep+1,result+arr1[dep])
            elif i==1:        
                perm(dep+1,result-arr1[dep])
            elif i==2:        
                perm(dep+1,result*arr1[dep])
            elif i==3:        
                perm(dep+1,int(result/arr1[dep]))
            arr[i]+=1
t= int(input())
for tc in range(1,t+1):
    n= int(input())
    arr= list(map(int,input().split()))
    arr1=list(map(int,input().split()))
    max_v = -float('inf')
    min_v = float('inf')    
    perm(1,arr1[0])
    s=max_v-min_v
    print(f'#{tc} {s}')
