from collections import deque

n, m = map(int,input().split())
grid = []
for _ in range(n):
    grid.append( list(map(int,input().split())) )
visited = [ [True for _ in range(m)] for _ in range(n) ]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 0 or visited[x][y]:
        return False
    return True

q = deque()
q.append((0,0))
visited[0][0] = True

dx, dy = [-1,1,0,0], [0,0,-1,1]
while q:
    x,y = q.popleft()
    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if can_go(nx,ny):
            visited[nx][ny] = True
            q.append((nx,ny))

if visited[n-1][m-1] == True:
    print(1)
else:
    print(0)