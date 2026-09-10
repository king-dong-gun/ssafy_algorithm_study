import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for i in range(N):
        row = []

        for j in range(i + 1):
            if j == 0:
                row.append(1)
            elif j == i:
                row.append(1)
            else:
                value = arr[i - 1][j - 1] + arr[i -1][j]
                row.append(value)
        arr.append(row)


    print(f"#{test_case}")
    for row in arr :
        print(*row)