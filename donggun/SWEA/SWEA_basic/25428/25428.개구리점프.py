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

    ##========================
    # N: 5
    # K: 3
    # now_idx: 3
    # range(4, 7) -> 4, 5, 6
    # N이 5라서 아웃 오브 레인지
    # min(6, 4)+1
    # 마지막 범위 range(4, 5) -> 4, 5
    # N 5라서 아웃 오브 레인지 안남
    ##========================
    # 마지막 result에 min도 N을 넘으면 안되기 때문에