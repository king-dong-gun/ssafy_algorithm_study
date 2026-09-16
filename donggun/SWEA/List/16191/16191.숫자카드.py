import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().strip()))
    count = [0] * 10
    max_num = 0
    max_count = 0

    for i in range(N):
        count[num[i]] += 1
        if count[num[i]] > max_count:
            max_count = count[num[i]]
            max_num = num[i]

        elif count[num[i]] == max_count and num[i] > max_num :
            max_num = num[i]

    print(f"#{test_case} {max_num} {max_count}")


