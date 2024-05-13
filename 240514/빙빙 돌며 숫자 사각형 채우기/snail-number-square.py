n, m = map(int,input().split())

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

d2 = [ [0 for _ in range(m)] for _ in range(n)]

dd = {'U':0,'R':1,'D':2,'L':3}
dx, dy = [-1,0,1,0], [0,1,0,-1]

x,y= 0, 0
d_num = 1
for i in range(1,n*m+1):
    if in_range(x,y) and d2[x][y] == 0:
        d2[x][y] = i
        x, y = x+dx[d_num], y+dy[d_num]
    else :
        x, y = x-dx[d_num],y-dy[d_num]
        d_num = (d_num+1)%4
        x, y = x+dx[d_num], y+dy[d_num]
        d2[x][y] = i
        x, y = x+dx[d_num], y+dy[d_num]
for k in d2:
    for h in k:
        print(h, end=" ")
    print()