n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append( list(map(int,input().split())) )
visited = [ [False for _ in range(m)] for _ in range(n) ]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    if not in_range(x,y):
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    else:
        return True

dx, dy = [1,0],[0,1]
def dfs(x,y):
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]

        if can_go(nx,ny):
            visited[nx][ny] = True
            dfs(nx,ny)

visited[0][0] = True
dfs(0,0)

if visited[n-1][m-1]:
    print(1)
else:
    print(0)