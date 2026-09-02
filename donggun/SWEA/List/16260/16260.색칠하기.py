import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

white = 0
red = 1
blue = 2
purple = 3

for test_case in range(1, T + 1):

    result = 0

    N = int(input())
    # 배열 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * 10 for _ in range(10)]

    for area in arr:
        row1, col1, row2, col2, color = area

        for row in range(row1, row2 + 1):
            for col in range(col1, col2 + 1):
                board[row][col] += color



    for row in range(10):
        for col in range(10):
            if board[row][col] == purple:
                result += 1


    print(f"#{test_case} {result}")