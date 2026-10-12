def dfs(m, cost):
    global max_money
    if cost >= max_money:
        return
    # 12월을 넘었다면
    if m > 12:
        max_money = cost
        return
    # 1일권/1달권
    dfs(m+1, cost + min(arr[m] * day, one_month))
    # 3달권
    dfs(m+3, cost+three_month)


T = int(input())
for tc in range(1, T+1):
    day, one_month, three_month, year = map(int, input().split())
    arr = [0] + list(map(int, input().split()))
    max_money = year
    # m = month, cost(최대 비용 담을 변수)
    dfs(1, 0)
    print(f"#{tc} {max_money}")