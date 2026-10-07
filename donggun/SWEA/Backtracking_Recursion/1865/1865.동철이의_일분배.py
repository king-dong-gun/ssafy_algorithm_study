import sys
sys.stdin = open("input (11).txt", "r")

T = int(input())














for test_case in range(1, T + 1):
    N = int(input())
    arr = []

    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)