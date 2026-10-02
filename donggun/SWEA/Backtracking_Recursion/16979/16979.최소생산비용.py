import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())


def recursive(i, cost):
    global min_cost

    # 가지치기
    if cost >= min_cost:
        return

    # 모든 제품을 배정했다면
    if i == N:
        # 최소 비용 갱신
        min_cost = min(cost, min_cost)
        return

    # 재귀호출
    for j in range(N):
        # 이미 사용한 공장이면 넘어가기
        if visited[j] == 1:
            continue
        visited[j] = 1
        recursive(i + 1, cost + factory[i][j])
        visited[j] = 0


for test_case in range(1, T + 1):
    # 입력의 첫 숫자는 N : 제품 갯수
    # factory : 공장별 생산비용
    N = int(input())
    factory = []
    visited = [0] * N
    min_cost = 999999

    for _ in range(N):
        row = list(map(int, input().split()))
        factory.append(row)

    recursive(0, 0)

    print(f"#{test_case} {min_cost}")



