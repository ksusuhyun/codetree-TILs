from collections import deque
n, k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
visitied = [ [False for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

def can_go(x,y):
    if not in_range(x,y):
        return False
    if grid[x][y] == 1 or visitied[x][y]:
        return False
    return True

q = deque()
dx, dy = [-1,1,0,0],[0,0,-1,1]
def bfs():
    for _ in range(k):
        sx, sy = map(int,input().split())
        q.append((sx-1,sy-1))
        visitied[sx-1][sy-1] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if can_go(nx,ny):
                visitied[nx][ny] = True
                q.append((nx,ny))
bfs()
res = 0
for i in visitied:
    res += i.count(True)

print(res)