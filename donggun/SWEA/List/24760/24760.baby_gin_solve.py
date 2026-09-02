import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    # 테스트 케이스마다 숫자 입력 하나
    numbers = int(input())

    # 카운트 배열
    # 각 자리의 숫자가 몇번 등장했는지 세어본다.
    counts = [0] * 12

    # 10으로 나눠서 마지막 자리를 땜 -> // or % 연산자 사용
    for i in range(6):
        # 1의 자리 수의 숫자를 떼어내고
        counts[numbers % 10] += 1
        # 다음 자리수로 이동한다.
        num = numbers // 10

    # run인지 triplet 인지 확인
    i = 0
    # baby gin 조건 run 횟수 + triplet 횟수
    triplet = run_cnt = 0

    while i < 10:
        # triplet 부터 확인
        if counts[i] >= 3:
            counts[i] -= 3
            triplet += 1
            # 같은 숫자에서 triplet 최대 두번 가능
            continue
        # run 확인
        if counts[i] >= 1 and counts[i+1] >= 1 and counts[i+2] >= 1:
            # i, i+1, i+2 숫자 하나씩 개수 차감
            counts[i] -= 1
            counts[i+1] -= 1
            counts[i+2] -= 1

            run_cnt += 1
            # 같은 숫자에서 run 최대 두번 가능
            continue

        # 다음 조건 확인
        i += 1

    # 출력
    if run_cnt + triplet == 2:
        print(f"#{test_case} Baby Gin")
    else:
        print(f"#{test_case} Loss")