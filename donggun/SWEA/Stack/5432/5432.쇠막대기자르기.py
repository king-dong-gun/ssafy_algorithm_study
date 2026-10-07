import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    arr = input().strip()

    stack = []
    result = 0

    for i in range(len(arr)):
        if arr[i] == "(":
            stack.append("(")
        else:
            stack.pop()

            if arr[i - 1] == "(":
                result += len(stack)
            else:
                result += 1

    print(f"#{test_case} {result}")