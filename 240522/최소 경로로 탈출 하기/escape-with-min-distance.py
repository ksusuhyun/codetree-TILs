from collections import deque
n, m = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [False for _ in range(m)] for _ in range(n) ]
step = [ [0 for _ in range(m)] for _ in range(n) ]

def in_range(x,y):
    return 0<=x<n and 0<=y<m

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 0 or visited[x][y]:
        return False
    return True

q = deque()
dx, dy = [-1,1,0,0],[0,0,-1,1]
def bfs():
    q.append((0,0))
    visited[0][0] = True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if can_go(nx,ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx,ny))

bfs()
if visited[n-1][m-1]:
    print(step[n-1][m-1])
else:
    print(-1)