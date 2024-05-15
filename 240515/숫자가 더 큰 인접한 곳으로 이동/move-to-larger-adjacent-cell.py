n, x, y = map(int,input().split())
x, y = x-1, y-1
grid = [list(map(int,input().split())) for _ in range(n)]
dx, dy = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

num = [grid[x][y]]
while True:
    flag = False
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if in_range(nx,ny) and grid[x][y] < grid[nx][ny] :
            flag = True
            num.append(grid[nx][ny])
            x, y = nx, ny
            break
    if not flag:
        break

for i in num:
    print(i, end=" ")