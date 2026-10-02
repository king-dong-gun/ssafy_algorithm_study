import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())


# 정류장 번호 : i
# count : 현재 i번 까지 오는데 충전한 횟수
def recursive(i, count):
    global min_count

    # 0. 가지치기
    # 이전에 내가 구한 최소 충전 횟수보다 현재 충전횟수가 같거나 크다면
    # 더 이상 진행할 필요가 없다.
    if count - 1 >= min_count:
        return

    # 1. 종료 조건 : 정류장 번호의 마지막 인덱스가 입력값 N보다 크거나 작으면 종료
    if i >= N - 1:
        # 현재 충전한 횟수가 최소값인지 판단하고 갱신
        # 출발지 충전 횟수는 세지 않으니 count - 1
        min_count = min(count - 1, min_count)
        return

    # 2. 재귀 호출 : 다음 단계로 넘어갈 수 있는 경우의 수 (branch)
    # 현재 정류장 번호는 i, 현재 정류장의 충전 용량은 bus_stop[i]
    # 다음 갈 수 있는 거리는 1 ~ bus_stop[i]
    for j in range(1, bus_stop[i] + 1):
        # 충전횟수 +1, 다음에 갈 정류장 번호는 i+j번
        recursive(i + j, count + 1)


for test_case in range(1, T + 1):
    # 입력의 첫 숫자는 N : 정류장 개수
    # 나머지 숫자들은 bus_stop : 각 정류장의 충전지 용량
    N, *bus_stop = map(int, input().split())
    min_count = 999999

    recursive(0, 0)

    print(f"#{test_case} {min_count}")



