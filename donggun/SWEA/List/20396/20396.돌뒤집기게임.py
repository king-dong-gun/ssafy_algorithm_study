import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # N개의 돌, M개의 줄
    N, M = map(int, input().split())
    # 돌의 초기상태
    stones = list(map(int, input().split()))

    for command in range(M):
        # M번의 입력, i번째의 돌부터 j개의 돌 뒤집기
        i, j = map(int, input().split())
        start_idx = i - 1
        start_color = stones[start_idx]

        for next_idx in range(start_idx, min(start_idx + j, N)):
            stones[next_idx] = start_color

    print(f"#{test_case}", *stones)

