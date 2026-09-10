import sys
sys.stdin = open("sample_input.txt", "r")
# N인 물웅덩이
# 거리는 최대 K
# 물웅덩이의 정보 pond

T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())
    pond = list(map(int, input().split()))
    now_idx = 0

    for i in range(N):
        if now_idx == N - 1:
            break

        # 범위 => 현재위치+1 ~ (현재위치+점프거리, 연못길이-1) 중 더 작은 값 + 1
        for next_idx in range(now_idx+1, min(now_idx + K, N - 1) + 1):
            if pond[next_idx] == 1:
                now_idx = next_idx

    result = min(now_idx + K + 1, N)
    print(f"#{test_case} {result}")
