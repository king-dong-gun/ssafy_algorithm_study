import sys
sys.stdin = open("sample_input(1).txt", "r")

from collections import deque


def find_start(maze, N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == "2":
                return i, j


def bfs(i, j, N):
    visited = [[0] * N for _ in range(N)]

    q = [(i, j)]
    visited[i][j] = 1

    while q:
        ti, tj = q.pop(0)

        # 도착점이면 2와 3 사이의 거리 반환
        if maze[ti][tj] == "3":
            return visited[ti][tj] - 2

        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = ti + di
            nj = tj + dj

            if (
                    0 <= ni < N
                    and 0 <= nj < N
                    and maze[ni][nj] != "1"
                    and visited[ni][nj] == 0
            ):
                q.append((ni, nj))
                visited[ni][nj] = visited[ti][tj] + 1

    return 0


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    maze = [input() for _ in range(N)]

    start_i, start_j = find_start(maze, N)

    result = bfs(start_i, start_j, N)

    print(f"#{test_case} {result}")