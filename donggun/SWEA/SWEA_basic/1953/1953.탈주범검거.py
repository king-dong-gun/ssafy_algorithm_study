import sys
sys.stdin = open("sample_input.txt", "r")

# 오른쪽 0
# 아래 1
# 왼쪽 2
# 위쪽 3

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

pipe = [
    [],
    [0, 1, 2, 3],
    [1, 3],
    [0, 2],
    [0, 3],
    [0, 1],
    [1, 2],
    [2, 3]
]


def f(N, M, R, C, L):
    count = 0

    hole = [(R, C)]

    location = [[0] * M for _ in range(N)]
    location[R][C] = 1

    while hole:
        i, j = hole.pop(0)

        count += 1

        if location[i][j] < L:

            for x in pipe[tunnel[i][j]]:
                ni = i + di[x]
                nj = j + dj[x]

                if (
                    0 <= ni < N
                    and 0 <= nj < M
                    and tunnel[ni][nj] != 0
                    and location[ni][nj] == 0
                    and (x + 2) % 4 in pipe[tunnel[ni][nj]]
                ):
                    hole.append((ni, nj))
                    location[ni][nj] = location[i][j] + 1

    return count


T = int(input())

for test_case in range(1, T + 1):

    N, M, R, C, L = map(int, input().split())

    tunnel = [
        list(map(int, input().split()))
        for _ in range(N)
    ]

    result = f(N, M, R, C, L)

    print(f"#{test_case} {result}")