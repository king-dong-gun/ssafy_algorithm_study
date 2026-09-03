n, m = map(int, input().split())
grid = []
for i in range(n):
    grid.append(list(map(int, input())))

def dfs(r, c):
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False
    if grid[r][c] == 0:
        grid[r][c] = 1
        dfs(r-1, c)
        dfs(r+1, c)
        dfs(r, c-1)
        dfs(r, c+1)
        return True
    return False
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
print(result)


"""
6 8
00110011
00110011
11111111
00110000
00110110
11111111

8 5
00100
11111
00001
01001
01001
01111
00000
11111

5 9
001000100
001000100
111111111
100001001
100001001

"""
