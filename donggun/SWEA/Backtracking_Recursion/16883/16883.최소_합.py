import sys
sys.stdin = open("sample_input (4).txt", "r")

# 배열 범위 검증 함수
def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


# i, j 행, 열 번호
# sum_value 지나온 값들의 합
def recursive(x, y, sum_value):
    global answer

    # 가지치기
    if sum_value >= answer:
        return
    # 도착점 처리
    if (x, y) == (N - 1, N - 1):
        answer = min(answer, sum_value)
        return

    # 재귀호출
    # 오른쪽 아래 방향 설정
    for direction in range(2):
        ni = x + di[direction]
        nj = y + dj[direction]

        # 배열의 범위가 넘어가는지 확인
        if is_valid(ni, nj):
            recursive(ni, nj, sum_value + arr[ni][nj])


T = int(input())

di = [0, 1]
dj = [1, 0]

for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    answer = 10000
    # (0, 0, 1)
    # 0, 0 일때 sum_value가 1이다.
    recursive(0, 0, arr[0][0])

    print(f"#{test_case} {answer}")


