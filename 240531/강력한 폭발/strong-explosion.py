import copy

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

Dx = {1: [-1, 1, -2, 2], 2: [-1, 1, 0, 0], 3: [-1, -1, 1, 1]}
Dy = {1: [0, 0, 0, 0], 2: [0, 0, -1, 1], 3: [-1, 1, -1, 1]}

one = []
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            one.append((i, j))

N = len(one)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def Bomb(i, now, grid_copy):
    x, y = now[0], now[1]
    for inx in range(4):
        nx, ny = x + Dx[i][inx], y + Dy[i][inx]
        if in_range(nx, ny):
            grid_copy[nx][ny] = 1

def count(grid_copy):
    cnt = 0
    for row in grid_copy:
        cnt += row.count(1)
    return cnt

res = []
def choice(curr_num, grid_copy):
    if curr_num >= N:
        res.append(count(grid_copy))
        return
    for i in range(1, 4):
        new_grid_copy = copy.deepcopy(grid_copy)
        Bomb(i, one[curr_num], new_grid_copy)
        choice(curr_num + 1, new_grid_copy)

choice(0, grid)
print(max(res))