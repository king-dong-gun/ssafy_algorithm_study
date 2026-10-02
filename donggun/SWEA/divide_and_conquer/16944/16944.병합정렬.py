import sys
sys.stdin = open("sample_input(2) (1).txt", "r")

def merge_sort(m):
    global count
    if len(m) == 1:
        return m
    # ====================분할====================
    mid = len(m) // 2
    # m[: mid] -> left
    left = m[: mid]
    # m[mid :] -> right
    right = m[mid :]

    # ====================정복====================
    left = merge_sort(left)
    right = merge_sort(right)
    # 정렬 직후 마지막 원소 비교
    if left[-1] > right[-1]:
        count += 1

    # ====================합병====================
    return merge(left, right)

def merge(left, right):
    # 최소값의 위치
    left_index = right_index = 0

    result = []

    while left_index < len(left) or right_index < len(right):
        if left_index < len(left) and right_index < len(right):
            if left[left_index] <= right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1

        elif left_index < len(left):
            result.append(left[left_index])
            left_index += 1
        elif right_index < len(right):
            result.append(right[right_index])
            right_index += 1

    return result

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    count = 0

    sorted_arr = merge_sort(arr)

    print(f"#{test_case} {sorted_arr[N // 2]} {count}")

