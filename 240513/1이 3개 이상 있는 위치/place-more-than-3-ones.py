n = int(input())
num = [
    list(map(int,input().split()))
    for i in range(n)
]

def in_range(x,y):
    if 0 <= x and x < n and 0 <= y and y < n:
        return 1

res = 0
dx, dy = [1,-1,0,0], [0,0,-1,1]
for i in range(n):
    for j in range(n):
        x, y = i, j
        cnt = 0
        for dx_,dy_ in zip(dx,dy):
            nx, ny = x+dx_, y+dy_
            if in_range(nx,ny) and num[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            res += 1
print(res)