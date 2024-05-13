n = int(input())
x, y = 0, 0
for i in range(n):
    d, w = input().split()
    w = int(w)
    if d == 'S':
        y -= w
    elif d == 'N':
        y += w
    elif d == 'E':
        x += w
    else:
        x -= w
print(x,y)