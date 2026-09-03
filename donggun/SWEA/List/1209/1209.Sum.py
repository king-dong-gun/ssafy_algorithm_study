import sys

sys.stdin = open("sum_input.txt", "r")

T = int(input())
T = 10
for test_case in range(1, T + 1):
# for test_case in range(1, 11):
    if test_case > 1:
        input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    max_num = 0
    # 행 합
    for row in range(100):
        total = 0

        for col in range(100):
            total += arr[row][col]

            if total > max_num:
                max_num = total
    # 열 합
    for col in range(100):
        total = 0

        for row in range(100):
            total += arr[row][col]

            if total > max_num:
                max_num = total

    total = 0
    # 대각선 합
    for i in range(100):
        total += arr[i][i]

        if total > max_num:
            max_num = total

    total = 0

    for i in range(100):
        total += arr[i][99 - i]

        if total > max_num:
            max_num = total

    print(f"#{test_case} {max_num}")
