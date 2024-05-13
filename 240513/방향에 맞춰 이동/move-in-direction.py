n = int(input())
x, y = 0, 0
dx, dy = [1,-1,0,0],[0,0,-1,1]
for i in range(n):
    d, w = input().split()
    w = int(w)
    if d == 'E':
        d_num = 0 
    elif d == 'W':
        d_num = 1
    elif d == 'S':
        d_num = 2
    else:
        d_num = 3

    x,y = x+dx[d_num]*w, y+dy[d_num]*w 
print(x,y)