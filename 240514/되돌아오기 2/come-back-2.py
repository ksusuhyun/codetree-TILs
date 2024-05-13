s = input()
s = list(s)

dd = {'N':0,'E':1,'S':2,'W':3}
dx, dy = [0,1,0,-1],[1,0,-1,0]
d_num = dd['N']
x, y = 0, 0

t = 0
cut = 0
for i in s:
    if i == 'R':
        d_num = (d_num + 1) % 4
        t += 1
    elif i == 'L':
        d_num = (d_num + 4 - 1) % 4
        t += 1
    else:
        x, y = x+dx[d_num], y+dy[d_num]
        t += 1
        
    if (x,y) == (0,0):
        cut += 1
        break
if cut == 0:
    print(-1)
else:
    print(t)