import sys
from collections import deque
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    q = deque(map(int, input().split()))

    for i in range(M):
        x = q.popleft()
        q.append(x)
    print(f"#{test_case} {q[0]}")