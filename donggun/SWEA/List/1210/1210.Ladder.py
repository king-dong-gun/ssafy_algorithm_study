import sys
sys.stdin = open("input.txt", "r")

T = 10

for test_case in range(1, T + 1):
    # 테스트 케이스 입력
    input()
    # 100줄 입력
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 맨 아래부터 시작
    y = 99
    x = ladder[99].index(2)

    while y > 0:
        # 왼쪽
        if x > 0 and ladder[y][x - 1] == 1:
            while x > 0 and ladder[y][x - 1] == 1:
                x -= 1
        # 오른쪽
        elif x < 99 and ladder[y][x + 1] == 1:
            while x < 99 and ladder[y][x + 1] == 1:
                x += 1

        y -= 1

    print(f"#{test_case} {x}")
