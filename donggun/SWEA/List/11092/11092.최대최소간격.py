import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    ai = list(map(int, input().split()))
    max_idx = 0
    min_idx = 0

    for i in range(N):
        if ai[i] >= ai[max_idx]:
            max_value = ai[i]
            max_idx = i
        if ai[i] < ai[min_idx]:
            min_idx = i

        result = abs(max_idx - min_idx)

    print(f"#{test_case} {result}")


