import sys
sys.stdin = open("input.txt", "r")
from collections import deque


for test_case in range(10):
    T = int(input())
    q = deque(map(int, input().split()))
    decrease = 1

    while True:
        x = q.popleft()
        x -= decrease

        if x <= 0:
            x = 0
            q.append(x)
            break

        q.append(x)

        decrease += 1

        if decrease > 5:
            decrease = 1

    print(f"#{test_case}", *q)