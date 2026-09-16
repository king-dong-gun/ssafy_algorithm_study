import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())     # 전선의 개수
    arr = []
    count = 0
    arr.sort()           # A전봇대에 연결된 전선 높이 기준 오름차순 정렬
    for i in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    # A 기준으로 앞에 있는 전선과 비교
    for i in range(1, N):
        for j in range(i):
            # A에서는 j가 더 낮은데
            # B에서는 j가 더 높으면 서로 교차
            if arr[j][1] > arr[i][1]:
                count += 1
    print(f"#{test_case} {count}")
