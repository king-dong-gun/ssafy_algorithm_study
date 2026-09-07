import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # N: 글자판 크기, M: 회문 길이
    N, M = map(int, input().split())

    arr = [input() for _ in range(N)]
    answer = ""

    # 가로 방향에서 길이 M만큼 잘라 회문인지 확인
    for i in range(N):
        for j in range(N - M + 1):
            word = arr[i][j:j + M]   # 가로로 M개 자름

            if word == word[::-1]:
                answer = word

    # 세로 방향에서 같은 열의 문자를 M개 모아서 확인
    for j in range(N):
        for i in range(N - M + 1):
            word = ""

            for k in range(M):
                word += arr[i + k][j]    # 세로로 M개 모음

            if word == word[::-1]:   # 회문인지 확인
                answer = word

    print(f"#{test_case} {answer}")