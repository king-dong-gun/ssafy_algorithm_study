import sys
sys.stdin = open("input.txt", "r")

# T = int(input())

# for test_case in range(1, 10):
N = int( input())
boxes = list(map(int, input().split()))
max_drop = 0

for current_idx in range(N):
    drop_count = 0

    for next_idx in range(current_idx + 1, N):
        if boxes[next_idx] < boxes[current_idx]:
            drop_count += 1

            if drop_count > max_drop:
                max_drop = drop_count

print(f"{max_drop}")