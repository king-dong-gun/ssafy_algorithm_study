import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    tc = int(input())                           # 테스트 케이스 번호
    scores = list(map(int, input().split()))    # 학생 1000명의 점수

    counts = [0] * 101

    # 각 점수가 몇 번 나왔는지 카운트
    for score in scores:
        counts[score] += 1

    max_count = 0
    answer = 0

    # 가장 많이 나온 점수 찾기
    for score in range(101):
        if counts[score] >= max_count:
            max_count = counts[score]
            answer = score

    print(f"#{tc} {answer}")