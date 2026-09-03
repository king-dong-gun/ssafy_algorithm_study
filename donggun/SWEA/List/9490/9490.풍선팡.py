import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    # 꽃가루 개수가 들어있는 2차원 리스트 입력
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flower = 0

    for row in range(N):
        for col in range(M):
            sum_flower = arr[row][col]

            for row_move, col_move in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                for distance in range(1, arr[row][col] + 1):
                    next_row = row + row_move * distance
                    next_col = col + col_move * distance

                    if 0 <= next_row < N and 0 <= next_col < M:
                        sum_flower += arr[next_row][next_col]


            if max_flower < sum_flower:
                max_flower = sum_flower

    print(f"#{test_case} {max_flower}")