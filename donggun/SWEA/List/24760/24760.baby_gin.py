import sys
sys.stdin = open("input.txt", "r")

def check(a, b, c):
    if a == b == c:
        return True
    if a + 1 == b and b + 1 == c:
        return True

    return False

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    is_babygin = False
    numbers = list(map(int, input().strip()))

    for i0 in range(6):
        for i1 in range(6):
            if i0 != i1:

                for i2 in range(6):
                    if i2 != i0 and i2 != i1:

                        for i3 in range(6):
                            if i3 != i0 and i3 != i1 and i3 != i2:

                                for i4 in range(6):
                                    if i4 != i0 and i4 != i1 and i4 != i2 and i4 != i3:

                                        for i5 in range(6):
                                            if i5 != i0 and i5 != i1 and i5 != i2 and i5 != i3 and i5 != i4:

                                                if check(numbers[i0], numbers[i1], numbers[i2]) and \
                                                        check(numbers[i3], numbers[i4], numbers[i5]):
                                                    is_babygin = True

    if is_babygin:
        print(f"#{test_case} Baby Gin")
    else:
        print(f"#{test_case} Lose")