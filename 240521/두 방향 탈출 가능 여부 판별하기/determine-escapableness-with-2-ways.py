n,m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append( list(map(int,input().split())) )
visited = [ [False for _ in range(m)] for _ in range(n) ]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

dx, dy = [1,0],[0,1]
def dfs(vertex):
    x, y = vertex[0], vertex[1]

    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]

        if in_range(nx,ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
            dfs((nx,ny))

start = (0,0)
visited[0][0] = True
dfs(start)

if visited[m-1][m-1]:
    print(1)
else:
    print(0)