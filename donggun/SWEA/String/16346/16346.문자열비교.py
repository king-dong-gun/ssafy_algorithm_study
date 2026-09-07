import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    answer = 0

    # str2에서 str1이 들어갈 수 있는 시작 위치를 확인
    for i in range(M - N + 1):

        # str1의 각 글자를 하나씩 비교
        for j in range(N):
            if str2[i + j] != str1[j]:
                break

        # break 없이 모든 글자가 같았다면 문자열 일치
        else:
            answer = 1
            break

    print(f"#{test_case} {answer}")