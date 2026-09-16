import sys
sys.stdin = open("sample_input.txt", "r")


def shoot(ball, count, org):
    global min_value

    # 구슬을 N번 다 쐈거나
    # 벽돌이 모두 없어졌으면 종료
    if ball == N or count == 0:
        min_value = min(min_value, count)
        return

    # 어느 열에 구슬을 쏠지 선택
    for j in range(W):

        # 원본 배열 복사
        dest = [row[:] for row in org]

        tmp = []
        n_count = count

        # 해당 열에서 가장 위에 있는 벽돌 찾기
        for i in range(H):
            if dest[i][j]:

                n_count -= 1

                # 폭발시킬 벽돌 저장
                tmp.append([i, j, dest[i][j]])

                # 현재 벽돌 제거
                dest[i][j] = 0
                break

        # 연쇄 폭발
        while tmp:
            i, j, p = tmp.pop()

            for k in range(1, p):
                for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:

                    ni = i + di * k
                    nj = j + dj * k

                    # 배열 범위 안이고 벽돌이 존재한다면
                    if 0 <= ni < H and 0 <= nj < W and dest[ni][nj]:

                        # 숫자가 2 이상이면 또 폭발해야 함
                        if dest[ni][nj] > 1:
                            tmp.append([ni, nj, dest[ni][nj]])

                        # 벽돌 제거
                        dest[ni][nj] = 0
                        n_count -= 1

        # 벽돌 아래로 떨어뜨리기
        for col in range(W):

            bottom = H - 1

            for row in range(H - 1, -1, -1):

                if dest[row][col] != 0:

                    dest[bottom][col] = dest[row][col]

                    if bottom != row:
                        dest[row][col] = 0

                    bottom -= 1

        # 다음 구슬 발사
        shoot(ball + 1, n_count, dest)


T = int(input())

for test_case in range(1, T + 1):

    # N = 구슬 개수
    # W = 가로
    # H = 세로
    N, W, H = map(int, input().split())

    arr = [
        list(map(int, input().split()))
        for _ in range(H)
    ]

    min_value = H * W

    # 처음 벽돌 개수
    block_num = 0

    for row in range(H):
        for col in range(W):
            if arr[row][col] != 0:
                block_num += 1

    shoot(0, block_num, arr)

    print(f"#{test_case} {min_value}")