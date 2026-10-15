def check(line):
    used = [False] * N

    for i in range(N - 1):
        now = line[i]
        next = line[i + 1]

        if now == next:
            continue
        if abs(now - next) >= 2:
            return False

        if now > next:
            # 내려가는 경사로
            for j in range(i + 1, i + 1 + X):
                if j >= N or line[j] != next or used[j]:
                    return False
                used[j] = True

        else:
            # 올라가는 경사로
            for j in range(i + 1 - X, i + 1):
                if j < 0 or line[j] != now or used[j]:
                    return False
                used[j] = True

    return True

T = int(input())
for tc in range(1, T+1):
    N, X = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    
    transposed = list(zip(*grid))
    ans = 0
    
    # 가로 검사
    for r in range(N):
        if check(grid[r]):
            ans += 1

    # 세로 검사
    for line in transposed:
        if check(line):
            ans += 1
            
    print(f'#{tc} {ans}')
    
"""

( 6 ≤ N ≤ 20 )
( 2 ≤ X ≤ 4 )
검사는 가로로 쭉 보고 그다음 세로로 쭉 보면 될거같음
높이의 제한은 1~6이므로
6부터 있는지 검사후 근처 X칸 전부 검사를해야함
어떻게 검사를 하느냐
일단 엣지를 찾아야함 엣지란 높이가 변화하는 구간임
6을 본다고하면 먼저 6이 있는지 확인하고 없으면 5 4 3 2 봄
그다음 거기서 인접한곳이 6인지 계속 검사하다가
6>5로 변화하는 구간을 감지후에 거기서부터 X칸을 검사해서 변화가 없어야함
근데 중요한게 봉우리가 2개이상 있는경우를 생각해야함
그래서 결국에 열이나 행을 싹다 5번(6 5 4 3 2)봐야함
N*2*5번 검사를 할건데 생각보다 그렇게 횟수가 많지않음 
대신에 가능한경우를 최대한 조기에 확인해서 가지치기하는 로직은 필요할것으로 보임
가능한경우를 어떻게아느냐 > 아무 문제없이 양쪽 끝까지 검사성공하면 가능한거임 그 아래숫자들 안보더라도

근데 이렇게 복잡하게 생각을 해야하는 문제인가 싶음
그냥 해당 행/열의 모든 칸에 대해서 인접한 X칸들이 전부 해당 칸 높이 -1 이거나 전부 해당칸과 높이가 같으면 avaliable
한 다음 언덕 한복판에 있거나 그리드 보더에 막히거나 하는경우를 예외처리하는 방식으로 발전시키는게?
언덕 복판에 있는경우는 X=2라고 치면 66665와 66656를 구분해야함
근데 2<=X<=4니까 걍 노가다해도 될지도?
[0, 0], [0, -1], [-1, -1]
문제가 이러면 6은 검사를 제대로 통과해도 5에서 검사할때 6을 만나면 제대로 동작안함
근데 그냥 어차피 두칸씩 작아지는건 더 높은 높이에서 미리 검사했으니 X칸 이내에 자기보다 높은 칸 있으면 걍 패스해도될지도
보더에 막히는 경우는 B5666 같은 경우를 예외처리해야함
"""
