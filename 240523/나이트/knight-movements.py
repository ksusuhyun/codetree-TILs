from collections import deque
n = int(input())
r1,c1,r2,c2 = map(int,input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n
def can_go(x,y):
    if not in_range(x,y):
        return False
    if visited[x][y]:
        return False
    return True

q = deque()
dx,dy = [-2,-1,1,2,2,1,-1,-2],[-1,-2,-2,-1,1,2,2,1]
def bfs():
    q.append((r1-1,c1-1))
    visited[r1-1][c1-1] = True

    while q:
        x,y = q.popleft()
        for i in range(8):
            nx,ny = x+dx[i], y+dy[i]

            if can_go(nx,ny):
                visited[nx][ny] = True
                step[nx][ny] = step[x][y] + 1
                q.append((nx,ny))

bfs()
if visited[r2-1][c2-1]:
    print(step[r2-1][c2-1])
else:
    print(-1)