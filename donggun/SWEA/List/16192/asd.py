T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    table=list(map(int, input().split()))
    min_boxes = table[0]
    min_position=1

    for i in range(N):
        if table[i] < min_boxes:
            min_boxes = table[i]
            min_position = 1 + i
    print(f"#{test_case} {min_boxes} {min_position}")
