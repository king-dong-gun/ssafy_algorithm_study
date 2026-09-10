import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M  = map(int, input().split())
    arr = []
    max_count = 0

    for i in range(N):
        flowers = list(map(int, input().split()))
        arr.append(flowers)

    for i in range(N):
        for j in range(M):

            current_value = arr[i][j]
            total = current_value

            # 상하좌우
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]

            # 델타는 4번 돔
            for direction in range(4):
                next_row = i + dr[direction]
                next_col = j + dc[direction]

                # 배열 밖인지 검사
                if 0 <= next_row < N and 0 <= next_col < M:
                    total += arr[next_row][next_col]

                    if total > max_count:
                        max_count = total
    print(f"#{test_case} {max_count}")


