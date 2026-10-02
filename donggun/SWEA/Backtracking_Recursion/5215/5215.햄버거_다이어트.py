import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def recursive(i, score, calorie):
    global max_score

    # 0. 가지치기
    if calorie > L:
        return

    # 1. 종료 조건
    if i == N:
        max_score = max(max_score, score)
        return

    # 2. 재귀 호출
    recursive(i + 1, score + arr[i][0], calorie + arr[i][1])
    recursive(i + 1, score, calorie)


for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    arr = []
    max_score = 0

    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)
    recursive(0, 0, 0)

    print(f"#{test_case} {max_score}")