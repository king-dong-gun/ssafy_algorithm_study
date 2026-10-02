import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    result = 1

    for i in range(1, N):
        if arr[i] >= arr[i - 1]:
            result = 0
            break

    print(f"#{test_case} {result}")