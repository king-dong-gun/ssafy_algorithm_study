import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    M = int(input())
    password = list(map(int, input()))
    password_idx = 0

    for i in arr:
        if i == password[password_idx]:
            password_idx += 1

            if password_idx == M:
                break

    if password_idx == M:
        result = 1
    else:
        result = 0

    print(f"#{test_case} {result}")
