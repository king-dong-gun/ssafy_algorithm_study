import sys
sys.stdin = open("sample_input (4).txt", "r")

T = int(input())


def recursive(current_num, visited, e):
    global answer

    # 가지치기
    if e >= answer:
        return

    # 모든 구역 방문 완료
    if len(visited) == N:
        e += arr[current_num][0]
        answer = min(answer, e)
        return

    # 재귀호출
    for i in range(N):
        if i not in visited:
            recursive(i, visited + [i], e + arr[current_num][i])


for test_case in range(1, T + 1):
    N = int(input())

    arr = []
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    answer = 10000

    recursive(0, [0], 0)

    print(f"#{test_case} {answer}")