n = int(input())
visited = [ list(map(int,input().split())) for _ in range(n)]

def in_range(x,y):
    return 0<=x<n and 0<=y<n

dx,dy = [-1,1,0,0],[0,0,-1,1]

def dfs(x,y):
    global people

    for i in range(4):
        nx,ny = x+dx[i], y+dy[i]
        if in_range(nx,ny) and visited[nx][ny] == 1:
            people += 1
            visited[nx][ny] = 0
            dfs(nx,ny)

# 1을 찾는 과정
cnt_p = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 1:
            visited[i][j] = 0
            people = 1

            dfs(i,j)
            cnt_p.append(people)

print(len(cnt_p))
for i in sorted(cnt_p):
    print(i)