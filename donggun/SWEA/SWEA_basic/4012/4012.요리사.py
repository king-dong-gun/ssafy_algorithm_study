import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    min_diff = float('inf')

    def recursive(start, count):
        global min_diff

        if count == N // 2:
            taste_a = 0
            taste_b = 0

            for i in range(N):
                for j in range(N):
                    if used[i] == 1 and used[j] == 1:
                        taste_a += S[i][j]
                    elif used[i] == 0 and used[j] == 0:
                        taste_b += S[i][j]

            diff = abs(taste_a - taste_b)
            min_diff = min(min_diff, diff)
            return

        for i in range(start, N):
            used[i] = 1
            recursive(i + 1, count + 1)
            used[i] = 0

    recursive(0, 0)

    print(f'#{tc} {min_diff}')