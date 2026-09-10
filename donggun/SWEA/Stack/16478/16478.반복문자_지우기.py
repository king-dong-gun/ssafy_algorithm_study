import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = input()

    top = -1
    stack = [0] * 1000

    for i in N:
        if top != -1 and stack[top] == i:
            top -= 1
        else:
            top += 1
            stack[top] = i

    print(f"#{test_case} {top + 1}")