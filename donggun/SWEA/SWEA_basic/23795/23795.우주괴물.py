import sys
sys.stdin = open("sample_in.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    arr = []

    # N x N 배열 입력
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    # 괴물 위치 찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                monster_i = i
                monster_j = j

    # 광선이 닿았는지 저장
    visited = [[False] * N for _ in range(N)]

    # 상, 하, 좌, 우
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 4방향 광선 발사
    for d in range(4):
        ray_i = monster_i + di[d]
        ray_j = monster_j + dj[d]

        # 배열 안에 있는 동안 계속 이동
        while 0 <= ray_i < N and 0 <= ray_j < N:

            # 벽 느끼면 그 방향 광선 종료
            if arr[ray_i][ray_j] == 1:
                break

            # 광선이 닿은 곳 표시
            visited[ray_i][ray_j] = True

            # 한 칸 더 이동
            ray_i += di[d]
            ray_j += dj[d]

    # 안전한 곳 카운트
    count = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and not visited[i][j]:
                count += 1

    print(f"#{test_case} {count}")