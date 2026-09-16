import sys
from collections import deque

sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    # 초기화
    visited = [[0] * M for _ in range(N)]
    q = deque()
    # 시작점 인큐/인큐표시
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                q.append((i, j))
                visited[i][j] = 1
    # 반복
    while q:
        ti, tj = q.popleft()
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni, nj = ti + di, tj + dj

            if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == "L" and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1

    print(f"#{test_case} {visited}")