T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    if n == 1:
        print(f'#{tc} {arr[0]}')
        continue
    d = [0]*(n+1)
    d[0] = arr[0]

    d[1] = max(arr[0], arr[1])
    for i in range(2, n):
        d[i] = max(d[i-1], d[i-2] + arr[i])
    print(f'#{tc} {d[n-1]}')
