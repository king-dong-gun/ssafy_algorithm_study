import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    visited = [0] * 1000001

    queue = []

    queue.append((N, 0))
    visited[N] = 1

    result = 0

    while queue:
        now, count = queue.pop(0)

        if now == M:
            result = count
            break

        next_numbers = [
            now + 1,
            now - 1,
            now * 2,
            now - 10
        ]

        for next_num in next_numbers:
            # 범위 검사
            if 1 <= next_num <= 1000000:
                if visited[next_num] == 0:
                    visited[next_num] = 1
                    queue.append((next_num, count + 1))


    print(f"#{test_case} {result}")