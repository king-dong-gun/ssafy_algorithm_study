import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    text = input()

    pair = {
        ")": "(",
        "}": "{"
    }

    # 스택 생성
    top = -1
    stack = [0] * 100

    answer = 1

    for i in text:
        if i in "{(":           # 여는 괄호면 push
            top += 1
            stack[top] = i
        elif i in ")}":         # 닫는 괄호면 꺼내서 확인
            if top == -1:       # 스택이 비어있으면
                answer = 0
                break
            else:               # 짝이 맞는지 확인
                top -= 1
                temp = stack[top + 1]
                if pair[i] != temp:
                    answer = 0
                    break
    if top != -1:
        answer = 0
    print(f"#{test_case} {answer}")


