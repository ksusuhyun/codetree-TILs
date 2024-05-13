n = int(input())
dx, dy = [1,-1,0,0], [0,0,-1,1]
x, y = 0, 0
sec = 0
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

    for j in range(w):
        x,y = x+dx[d_num], y+dy[d_num]
        sec += 1
        if x == 0 and y == 0:
            print(sec)
            break
            
if sec == 0:
    print(-1)