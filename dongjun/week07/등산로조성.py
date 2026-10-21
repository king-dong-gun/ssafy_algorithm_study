dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def go(nowr, nowc, depth, shaved, height):
    global ans
    ans = max(ans, depth)

    for d in range(4):
        nr = nowr + dr[d]
        nc = nowc + dc[d]

        if not (0 <= nr < N and 0 <= nc < N):
            continue

        if visited[nr][nc]:
            continue
        nxt = grid[nr][nc]
        visited[nr][nc] = True
        
        if nxt < height:    # 공사 없이 이동
            go(nr, nc, depth + 1, shaved, nxt)

        elif not shaved and nxt - K < height:   # 공사 하고 이동
            go(nr, nc, depth + 1, True, height - 1)
        visited[nr][nc] = False


T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    grid = []
    for _ in range(N):
        grid.append(list(map(int, input().split())))
    topheight = 0
    tops = []
    for r in range(N):
        for c in range(N):
            if topheight < grid[r][c]:
                topheight = grid[r][c]
                tops.clear()
                tops.append((r, c))
            elif topheight == grid[r][c]:
                tops.append((r, c))
    ans = 0
    visited = [[False] * N for _ in range(N)]
    for r, c in tops:
        visited[r][c] = True
        go(r, c, 1, False, grid[r][c])
        visited[r][c] = False
    print(f'#{tc} {ans}')
    

"""
① 등산로는 가장 높은 봉우리에서 시작해야 한다.

② 등산로는 산으로 올라갈 수 있도록 반드시 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 한다.
    즉, 높이가 같은 곳 혹은 낮은 지형이나, 대각선 방향의 연결은 불가능하다.

③ 긴 등산로를 만들기 위해 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎는 공사를 할 수 있다.

2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)

3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)

4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.

5. 지도에서 가장 높은 봉우리는 최대 5개이다.

6. 지형은 정수 단위로만 깎을 수 있다.

7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.


2     
5 1       
9 3 2 3 2 
6 3 1 7 5
3 4 8 9 9
2 3 7 7 7
7 6 5 5 8
3 2       
1 2 1     
2 1 2
1 2 1

현재 위치와 등산로 길이와 지형을 한번 깎았는지 여부를 인자로 넘기면 좋을거같음
지형을 깎는다면 무조건 최소한으로 깎는게 좋으니까 얼마나 깎는지까지는 계산할필요없음
대신에 현재높이+K-1 보다 크면 깎아도 못가는칸이고 반대로 현재높이보다 작으면 깎을 필요 없는칸임
인접한 칸이 전부다 현재높이 이상이거나 지형을 한번 깎았거나 안깎았어도 인접한칸이 전부 현재높이+K-1보다 크면 
등산로 길이 최댓값 갱신하면될것으로보임


"""
