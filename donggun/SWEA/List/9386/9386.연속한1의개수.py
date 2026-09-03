import sys
sys.stdin = open("input1.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    numbers = input().split("0")
    max_number = 0

    for number in numbers:
        if max_number < len(number):
            max_number = len(number)

    print(f"#{test_case} {max_number}")