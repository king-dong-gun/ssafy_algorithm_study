import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    arr = list(map(int, input().split()))

    for i in range(N - M + 1):
        total = 0

        for j in range(M):
            current = arr[i + j]
            total += current

        if i == 0:
            max_total = total
            min_total = total

        else:
            if total > max_total:
                max_total = total

            if total < min_total:
                min_total = total

        result = max_total - min_total
    print(f"#{test_case} {result}")