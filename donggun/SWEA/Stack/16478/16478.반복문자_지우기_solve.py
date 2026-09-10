import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    text = input()

    size = 1000
    top = -1
    stack = [0] * size

    for i in range(len(text)):
        if top == -1:
            top += 1
            stack[top] = text[i]
        # 스택에 비교할 글자가 있는 경우
        else:
            # top 문자와 현재 문자가 다르면 push
            if stack[top] != text[i]:
                top += 1
                stack[top] = text[i]
            else:
                top -= 1
    # 스택에 남아있는 원소의 개수 top + 1
    print(f"#{test_case} {top + 1}")