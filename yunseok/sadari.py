T = int(input())

# 좌 우 상  '하'는 pass
di = [0, 0, -1]
dj = [-1, 1, 0]

def up(lst, n):
    # 재귀 종료
    if n == 0:
        return 
    # 처리
    # 왼쪽 있는지 확인
    if arr[n + di[0]][lst + dj[0]] > 0:
        # 벽까지 가기

    # 오른쪽 있는지 확인
    elif arr[n + di[1]][lst + dj[1]] > 0:
        # 벽까지 가기
        
    # 위로 한칸     
    else:
        n += di[2]
        lst += dj[2] 

    # 재귀 함수
    up(lst-1, n -1)

# 10개 테스트 케이스 반복
for _ in range(10):
    arr = [list(map(int, input().split())) for _ in range(100)]
    # 열 갯수    N = len(arr)
    
    # 마지막 줄에서 2 찾기
    # 반복 (arr[마지막 줄]) 의 길이 만큼    len(arr[N])
    last = 0
    for las in range(100):
        # 100 번째 줄에서 2인 값 찾는 핵심 코드 N-1
        if arr[99][las] == 2:
            last = las
            break
    answer = up(last, 99)
    


print(f"{T} {answer}")