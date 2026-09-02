import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # 빈 종이
    paper = [[0] * 10 for _ in range(10)]

    # 보라색 칸의 개수
    purple = 0

    for _ in range(N):
        # 색칠 정보 입력 받기 (색칠 시작, 행번호, 열번호 색칠 마지막 행번호, 열번호, 색)
        i1, j1, i2, j2, color = list(map(int, input().split()))

        # (i1, j1) ~ (i2, j2)까지 color로 색칠
        for i in range(i1, i2 + 1):
            for j in range(j1, j2 + 1):
                # 0 흰색, 1 빨강색, 2 파랑색, 3 보라색
                paper[i][j] += color

                if paper[i][j] == 3:
                    purple += 1

    print(f"#{test_case} {purple}")