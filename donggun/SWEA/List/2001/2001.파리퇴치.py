import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())

    max_total = 0

    # 배열 생성
    arr = [list(map(int, input().split()))for _ in range(N)]
    for i in range(N):
        for j in range(N):
            # 파리채가 생성한 배열에서 범위를 넘어가는지 확인
            if i + M <= N and j + M <= N:
                total = 0

                # 파리 마리 수를 칸 마다 확인
                for x in range(M):
                    for y in range(M):
                        total += arr[i + x][j + y]

                        if total > max_total:
                            max_total = total

    print(f"#{test_case} {max_total}")
