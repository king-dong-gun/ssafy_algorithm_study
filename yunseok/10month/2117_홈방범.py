T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(N)]
    houses = [(i, j) for i in range(N) for j in range(N) if city[i][j]]
    ans = 0
    for r in range(N):
        for c in range(N):
            cnt = [0] * (2 * N)              # 거리별 집 개수
            for hr, hc in houses:
                cnt[abs(r - hr) + abs(c - hc)] += 1
            total = 0
            for K in range(1, N + 2):
                total += cnt[K - 1]          # 거리 K-1인 집 추가
                if total * M >= K * K + (K - 1) * (K - 1):
                    ans = max(ans, total)
    print(f"#{tc} {ans}")