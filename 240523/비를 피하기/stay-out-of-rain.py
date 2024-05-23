from collections import deque

n,h,m = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [False for _ in range(n)] for _ in range(n) ]
step = [ [0 for _ in range(n)] for _ in range(n) ]
res = [ [0 for _ in range(n)] for _ in range(n) ]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 1 or grid[x][y] == 2 or visited[x][y]:
        return False
    return True

q = deque()
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs():
    global cnt
    while q:
        x,y = q.popleft()

        if grid[x][y] == 3:
            return True

        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]

            if can_go(nx,ny):
                visited[nx][ny] = True
                q.append((nx,ny))
                cnt += 1

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            cnt = 0
            grid[i][j] = 0
            visited[i][j] = True
            q.append((i,j))
            if bfs():
                res[i][j] = cnt
                visited = [ [False for _ in range(n)] for _ in range(n) ]
                step = [ [0 for _ in range(n)] for _ in range(n) ]
            else:
                res[i][j] = -1
                visited = [ [False for _ in range(n)] for _ in range(n) ]
                step = [ [0 for _ in range(n)] for _ in range(n) ]
for i in res:
    print(*i)