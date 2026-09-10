# 가게 부품의 개수, 가게 부품 list
N = int(input())
N_arr = list(map(int, input().split()))
# 손님 부품의 개수, 손님이 원하는 부품 list
M = int(input())
M_arr = list(map(int, input().split()))


# 손님이 원하는 부품이 있는지 검사 * 1
def req(n):
    # n 손님이 원하는 부품
    # 포인터? 설정
    left = 0
    right = N - 1

    # 검사
    while left < right:
        mid = left + right
        point = N_arr[mid]

        if point > n:
            right = mid - 1
        elif point == n:
            return print("yes")
        elif point < n:
            left = mid + 1
    else:
        return print("no")


# 가게 부품 정렬
N_arr.sort()
# 함수를 M만큼 실행
for i in range(M):
    req(M_arr[i])

"""
5
8 3 7 9 2
3
5 7 9
"""