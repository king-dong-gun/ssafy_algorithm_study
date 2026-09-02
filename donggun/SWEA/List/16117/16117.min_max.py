
import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    max_num = max(numbers)
    min_num = min(numbers)

    result = max_num - min_num
    print(f"#{test_case} {result}")
