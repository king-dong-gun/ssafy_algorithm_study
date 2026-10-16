#4012 요리사 
def comb(start):
    global min_v
    if len(p)==n//2:
        a=p
        b=[]
        for i in range(n):
            if i not in a:
                b.append(i)
        a_sum=0
        b_sum=0
        for i in a:
            for j in a:
                if i != j:
                    a_sum += arr[i][j]
        for i in b:
            for j in b:
                if i != j:
                    b_sum += arr[i][j]

        min_v = min(min_v, abs(a_sum - b_sum))
        return
    
    for i in range(start,n):
        p.append(i)
        comb(i+1)
        p.pop()

t=int(input())
for tc in range(1,t+1):
    n=int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]

    p = []
    min_v = float('inf')
    comb(0)
    print(f"#{tc} {min_v}")