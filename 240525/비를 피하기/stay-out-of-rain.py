from collections import deque

n,h,m = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [False for _ in range(n)] for _ in range(n) ]
step = [ [0 for _ in range(n)] for _ in range(n) ]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 1 or visited[x][y]:
        return False
    return True

q = deque()
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 3:
                q.append((i,j))
                visited[i][j] = True

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                step[nx][ny] = step[x][y] + 1

bfs()

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            if step[i][j] == 0:
                step[i][j] = -1
        else:
            step[i][j] = 0

for i in step:
    print(*i)