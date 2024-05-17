n, m, t = map(int,input().split())
grid = [ list(map(int,input().split())) for _ in range(n) ]
glass = [ [0]*n for _ in range(n) ]
new_glass = [ [0]*n for _ in range(n) ]
for _ in range(m):
    r, c = map(int,input().split())
    r, c = r-1, c-1
    glass[r][c] = 1

dx, dy = [-1,1,0,0], [0,0,-1,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

for _ in range(t):
    for x in range(n):
        for y in range(n):
            if glass[x][y] == 1:
                max_ = 0
                for i in range(4):
                    nx, ny = x + dx[i], y + dy[i]
                    if in_range(nx,ny) and max_ < grid[nx][ny] :
                        max_ = grid[nx][ny]
                        mx, my = nx, ny
                # print(x,y,mx,my)
                glass[x][y] = 0
                new_glass[mx][my] += 1
    glass = new_glass
    new_glass = [ [0]*n for _ in range(n) ]

res = 0
for rr in range(n):
    for cc in range(n):
        if glass[rr][cc] == 1:
            res += 1
print(res)