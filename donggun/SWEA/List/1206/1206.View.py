import sys
sys.stdin = open("sample_input.txt", "r")

for test_case in range(1, 11):
    N = int(input())
    buildings = list(map(int, input().split()))

    answer = 0

    for i in range(2, N - 2):
        max_height = max(
            buildings[i - 2],
            buildings[i - 1],
            buildings[i + 1],
            buildings[i + 2]
        )

        if buildings[i] > max_height:
            answer += buildings[i] - max_height

    print(f"#{test_case} {answer}")
