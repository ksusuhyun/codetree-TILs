n = int(input())
visited = [ list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx,dy = [-1,1,0,0],[0,0,-1,1]

people = 0
def dfs(x,y):
    global people

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if in_range(nx,ny) and visited[nx][ny] == 1:
            people += 1
            visited[nx][ny] = 0
            dfs(nx,ny)

cnt_c = 0
cnt_p = []
while True:
    cnt_1 = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 1:
                cnt_1 += 1

    if cnt_1 == 0:
        break
    
    for i in range(n):
        if 1 in visited[i]:
            x, y = i, visited[i].index(1)
            break
    cnt_c += 1
    dfs(x,y)
    cnt_p.append(people)
    people = 0

print(cnt_c)
for i in sorted(cnt_p):
    print(i)