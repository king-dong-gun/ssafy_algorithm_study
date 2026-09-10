N = int(input())
bupum = list(map(int, input().split()))
M = int(input())
yochung = list(map(int, input().split()))
bupum.sort()
ans = []
for yo in yochung:
    left = 0
    right = len(bupum)-1
    found = False
    while left <= right:
        head = (left+right)//2
        if bupum[head] == yo:
            found = True
            ans.append('yes')
            break
        elif bupum[head] < yo:
            left = head+1
        elif bupum[head] > yo:
            right = head-1
    if not found:
        ans.append('no')
print(*ans)

        