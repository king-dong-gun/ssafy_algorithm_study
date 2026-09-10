import sys
sys.stdin = open("input.txt", "r")

T = 10
N = 8

for test_case in range(1, T + 1):
    M = int(input())

    array = []

    for _ in range(N):
        text = input().strip()
        array.append(text)

    count = 0

    for i in range(N):
        for j in range(N - M + 1):

            row_palindrome = True
            col_palindrome = True

            for k in range(M // 2):
                # 가로
                if array[i][j + k] != array[i][j + M - 1 - k]:
                    row_palindrome = False

                # 세로
                if array[j + k][i] != array[j + M - 1 - k][i]:
                    col_palindrome = False

            if row_palindrome:
                count += 1

            if col_palindrome:
                count += 1

    print(f"#{test_case} {count}")