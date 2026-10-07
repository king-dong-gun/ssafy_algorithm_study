import sys
sys.stdin = open("sample_input(1).txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    members = list(map(int, input().split()))

    p = [0] * (N + 1)

    def make_set(x):
        p[x] = x

    def find_set(x):
        if x != p[x]:
            p[x] = find_set(p[x])

        return p[x]

    def union(x, y):
        king_x = find_set(x)
        king_y = find_set(y)

        if king_x == king_y:
            return

        p[king_x] = king_y

    for i in range(1, N + 1):
        make_set(i)

    for i in range(0, M * 2, 2):
        x = members[i]
        y = members[i + 1]

        union(x, y)

    boss = []

    for i in range(1, N + 1):
        boss.append(find_set(i))

    result = len(set(boss))


    print(f"#{test_case} {result}")