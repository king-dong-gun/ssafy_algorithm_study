import sys

sys.stdin = open("sample_input.txt", "r")

# K = 이동 가능한 정류장 수
# N = 정류장 수
# M = 충전기 수


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K, N, M = map(int, input().split())
    charge = list(map(int, input().split()))

    # 변수 초기화
    current_location = 0
    charge_count = 0

    for i in range(N + 1):
        # 현재 위치 + 이동 가능한 정류장 수 >= 총 정류장 수면 stop
        if current_location + K >= N:
            break

        # 다음 정류장 초기화
        next_station = 0

        # 충전 수 확인
        for station in charge:
            # 현재 위치 < 충전소 <= 현재 위치 + 이동 가능한 정류장 수
            if current_location < station <= current_location + K:
                next_station = station

        # 다음 충전소가 없으면 종점까지 갈 수 없으므로 0
        if next_station == 0:
            charge_count = 0
            break

        # 다음 정류장을 현재 위치로 바꾸고 충전수를 1씩 올림
        current_location = next_station
        charge_count += 1

    print(f"#{test_case} {charge_count}")