from collections import deque
 
# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
 
# 각 방향의 반대 방향
opposite = [1, 0, 3, 2]
 
# 터널 종류별 이동 가능한 방향
tunnel = [
    [],             # 0: 터널 없음
    [0, 1, 2, 3],   # 1: 상하좌우
    [0, 1],         # 2: 상하
    [2, 3],         # 3: 좌우
    [0, 3],         # 4: 상우
    [1, 3],         # 5: 하우
    [1, 2],         # 6: 하좌
    [0, 2]          # 7: 상좌
]
 
 
def bfs(start_r, start_c):
    visited = [[0] * M for _ in range(N)]
 
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = 1
    count = 1
 
    while q:
        r, c = q.popleft()
 
        # 제한 시간에 도달하면 더 이동하지 않음
        if visited[r][c] == L:
            continue
 
        # 현재 터널에서 나갈 수 있는 방향만 확인
        for d in tunnel[board[r][c]]:
            nr = r + dr[d]
            nc = c + dc[d]
 
            if not (0 <= nr < N and 0 <= nc < M):
                continue
 
            if board[nr][nc] == 0 or visited[nr][nc]:
                continue
 
            # 다음 터널에 반대 방향 입구가 있어야 연결됨
            if opposite[d] not in tunnel[board[nr][nc]]:
                continue
 
            visited[nr][nc] = visited[r][c] + 1
            q.append((nr, nc))
            count += 1
 
    return count
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
 
    answer = bfs(R, C)
 
    print(f"#{tc} {answer}")