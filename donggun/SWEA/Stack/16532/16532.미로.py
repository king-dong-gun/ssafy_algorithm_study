import sys
sys.stdin = open("sample_input(2).txt", "r")

T = int(input())


def dfs(i, j, N):
    visited = [[0] * N for _ in range(N)]

    # 상하좌우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    stack = []
    visited[i][j] = 1

    while True:

        if maze[i][j] == 3:
            return 1

        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]

            if (
                    0 <= ni < N
                    and 0 <= nj < N
                    and not visited[ni][nj]
                    and maze[ni][nj] != 1
            ):
                stack.append((i, j))

                visited[ni][nj] = 1

                i, j = ni, nj

                break

        else:
            if stack:
                i, j = stack.pop()
            else:
                return 0


for test_case in range(1, T + 1):
    maze = []
    N = int(input())

    # 미로 입력
    for i in range(N):
        row = list(map(int, input()))
        maze.append(row)

    # 시작점 2 찾기
    si, sj = 0, 0

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si, sj = i, j

    result = dfs(si, sj, N)

    print(f"#{test_case} {result}")