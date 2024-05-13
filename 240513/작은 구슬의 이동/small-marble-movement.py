n, t = map(int,input().split())
x, y, d = input().split()
x, y = int(x), int(y)

def in_range(x,y):
    return 1 <= x and x < n+1 and 1 <= y and y < n+1

dd = {'U':0,'D':3,'L':2,'R':1}
d_num = dd[d]
dx, dy = [-1,0,0,1], [0,1,-1,0]

while t != 0:
    nx, ny = x+dx[d_num], y+dy[d_num]
    if in_range(nx,ny):
        t -= 1
        x, y = nx, ny
    else :
        t -= 1
        d_num = 3 - d_num
print(x, y)