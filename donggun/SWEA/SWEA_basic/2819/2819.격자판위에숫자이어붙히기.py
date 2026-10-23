import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, num):
    if len(num) == 7:       # 숫자 길이
        result.add(num)
        return

    for d in range(4):      # 이동 방향
        nx = x + dx[d]
        ny = y + dy[d]

        if 0 <= nx < 4 and 0 <= ny < 4:  # 격자 크기
            dfs(nx, ny, num + arr[nx][ny])


for tc in range(1, T + 1):
    arr = [input().split() for _ in range(4)]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(i, j, arr[i][j])

    print(f'#{tc} {len(result)}')