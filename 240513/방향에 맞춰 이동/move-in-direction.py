n = int(input())
dx, dy = [0,0,0,0], [0,0,0,0]
dd = []
for i in range(n):
    d, w = input().split()
    w = int(w)
    dd.append(d)
    if d == 'S':
        dy[0] = -1*w
    elif d == 'N':
        dy[1] = w
    elif d == 'E':
        dx[2] = w
    else:
        dx[3] = w
x, y = 0, 0
for i in dd:
    if i == 'S':
        y = y + dy[0]
    elif i == 'N':
        y = y + dy[1]
    elif i == 'E':
        x = x + dx[2]
    else:
        x = x + dx[3]
print(x,y)