import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())

    # B = C면 0이기 때문에 C-1
    count_candy = 0
    if B >= C:
        count_candy += B - (C - 1)
        B = C - 1

    # A = B면 0이기 때문에 B-1
    if A >= B:
        count_candy += A - (B - 1)
        A = B - 1

    # 하나라도 없으면 조건 만족x
    if A < 1 or B < 1 or C < 1:
        count_candy = -1

    print(f"#{test_case} {count_candy}")
