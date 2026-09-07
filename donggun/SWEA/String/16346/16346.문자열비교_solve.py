import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()

    result = 0

    # 마지막 시작 인덱스 = 전체 길이 - 찾을 문자열 길이
    # = len(str2) - len(str1)
    for i in range(len(str2) - len(str1) + 1):
        # str2의 i 위치에서 str1 길이만큼 슬라이싱
        # 이후 str1과 같은지 비교
        if str2[i: i + len(str1)] == str1:
            result = 1
            break

    print(f"#{test_case} {result}")