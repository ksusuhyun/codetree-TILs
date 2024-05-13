n = int(input())
dd = {'E':0,'W':1,'S':2,'N':3}
dx, dy = [1,-1,0,0],[0,0,-1,1]

x,y = 0,0
t = 0
cut = 0
for i in range(n):
    d, w = input().split()
    w = int(w)
    for j in range(w):
        x, y = x+dx[dd[d]], y+dy[dd[d]]
        t += 1
        if (x,y) == (0,0):
            cut += 1
            break
    if cut == 1:
        break

if t == 0:
    print(-1)
else:
    print(t)