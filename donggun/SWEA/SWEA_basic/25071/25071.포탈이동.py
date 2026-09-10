import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    portal = [0] + list(map(int, input().split()))
    current_room = 1
    visited = [0] * (N + 1)
    count = 0

    while current_room != N:
        if current_room == 1:
            current_room = 2
            count += 1
        else:
            if visited[current_room] == 0:
                visited[current_room] = 1
                current_room = portal[current_room]
                count += 1
            else:
                current_room += 1
                count += 1

    print(f"#{test_case} {count}")