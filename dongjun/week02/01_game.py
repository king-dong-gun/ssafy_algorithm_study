H, W = map(int, input().split())
startX, startY, startside = map(int, input().split())      # 바닥 상태 0 = 육지(아직안가봄), 1 = 바다, 2 = 육지(가본곳)
arr = []
for i in range(H):
    arr.append(list(map(int, input().split())))
steps = 1
arr[startX][startY] = 2
def test(x, y, side):                                  # 0 = 상(-1, 0), 1 = 우(0, 1), 2 = 하(1, 0), 3 = 좌(0, -1)
    global steps
    neighbors = [arr[x-1][y], arr[x][y+1], arr[x+1][y], arr[x][y-1]]
    if 0 in neighbors:
        if side == 0:                       # 상방향 진행일 경우
            if arr[x-1][y] == 0:            # 안가본 육지면 진행
                x -= 1
                arr[x][y] = 2               # 간 곳으로 체크
                steps += 1                  # 밟은 땅 하나 추가
            else:
                side += 1                   # 진행하는 곳이 가본곳이나 바다면 방향 +1 (우회전)
        elif side == 1:                     # 우향인 경우
            if arr[x][y+1] == 0:   
                y += 1
                arr[x][y] = 2
                steps += 1
            else:
                side += 1
        elif side == 2:
            if arr[x+1][y] == 0:
                x += 1
                arr[x][y] = 2
                steps += 1
            else:
                side += 1
        else:
            if arr[x][y-1] == 0:
                y -= 1
                arr[x][y] = 2
                steps += 1
            else:
                side = 0
        return test(x, y, side)             # 한칸 갔으면 재귀
    else:                                   # 모든 방향 갔거나 바다인경우
        if side == 0:                       # 상방향 진행일 경우
            if arr[x+1][y] == 2:            # 가본 육지면 후진
                x += 1
            else:
                return steps                # 뒤에 바다면 가본 땅 수 출력하면서 끝
        elif side == 1:                     # 우향인 경우
            if arr[x][y-1] == 2:   
                y -= 1
            else:
                return steps
        elif side == 2:
            if arr[x-1][y] == 2:
                x -= 1
            else:
                return steps
        elif side == 3:
            if arr[x][y+1] == 2:
                y += 1
            else:
                return steps
        return test(x, y, side)             # 한칸 갔으면 재귀

print(test(startX, startY, startside))