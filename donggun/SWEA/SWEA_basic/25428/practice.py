import sys
sys.stdin = open("input.txt", "r")

# N 도로 길이
# K 연속된 위치

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    max_total = 0

    for start_idx in range(N - K + 1):
        total = 0

        for next_idx in range(K):
            current = arr[start_idx + next_idx]
            total += current

        if total > max_total:
            max_total = total

    print(f"#{test_case} {max_total}")