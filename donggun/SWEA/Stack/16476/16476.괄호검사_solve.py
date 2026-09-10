import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    code = input()

    # 괄호 검사에 사용할 스택 생성
    stack = []

    pair = {
        ")": "(",
        "}": "{"
    }

    # 문제에서 원하는 답 -> 괄호가 제대로 되어있는가?
    # 일단 되어있다고 가정하고, 제대로 안된 조건 발견시 변경
    answer = 1

    for char in code:
        # 검사할 코드에서 한글자 가져와 char라고 한다.
        # 이 문제는 char가 괄호인 경우만 신경쓰면 된다.
        # 여는 괄호를 만나면 stack에 저장
        if char in "{(":
            stack.append(char)

        # 닫는 괄호를 만나면 스택에서 가장 최근에 저장한 괄호를 하나 꺼내
        # 모양이 맞는지 확인
        if char in "})":
            # 스택에 꺼낼 괄호가 남아있는지 확인
            # 남아있지 않다면?
            # 오른쪽 (닫는 괄호)의 개수가 더 많은 상황
            if not stack:
                answer = 0
                break

            # 스택에서 괄호 짝이 맞는지 확인
            left = stack.pop()
            if pair[char] != left:
                # 현재 보고 있는 닫는괄호가 char
                # 스택에서 꺼낸 왼쪽 괄호가 left
                answer = 0
                break
    # 코드 확인이 끝나고 스택에 왼쪽 괄호가 남아있다면
    # 왼쪽 괄호의 개수가 오른쪽 괄호보다 더 많은 상황
    if stack:
        answer = 0
    print(f"#{test_case} {answer}")
