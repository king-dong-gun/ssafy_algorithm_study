import sys
from math import factorial

sys.stdin = open("sample_input.txt", "r")

T = int(input())

def recursive(i, left, right):
    global count

    # 가지 치기 1
    if right > left:
        return

    # 종료 조건
    if i == N:
        count += 1
        return

    if left >= right + (total - left - right):
        count += factorial(N - i) * (2 ** (N - i))
        return

    for j in range(N):
        if used[j] == 1:
            continue

        used[j] = 1
        recursive(i + 1, left + coin[j], right)

        if left >= right + coin[j]:
            recursive(i + 1, left, right + coin[j])

        used[j] = 0


for test_case in range(1, T + 1):
    N = int(input())
    coin = list(map(int, input().split()))
    used = [0] * N
    total = sum(coin)
    count = 0

    recursive(0, 0, 0)
    print(f"#{test_case} {count}")