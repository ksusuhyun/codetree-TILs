s = input()

dx,dy =[0,1,0,-1],[1,0,-1,0]
x, y = 0,0
current = 0
for i in s:
    if i == 'L':
        current = (current + 4 - 1) % 4
    elif i == 'R':
        current = (current + 1) % 4
    else:
        x,y = x+dx[current], y+dy[current]
print(x, y)