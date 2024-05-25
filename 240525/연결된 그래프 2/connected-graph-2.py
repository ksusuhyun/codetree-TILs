n, m = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
visited = [ False for _ in range(n+1) ]

def dfs(curr):
    global cnt
    visited[curr] = True
    cnt += 1

    for next_ in graph[curr]:
        if not visited[next_]:
            visited[next_] = True
            dfs(next_)

cnt_ = []
for i in range(1,n+1):
    cnt = 0
    dfs(i)
    cnt_.append(cnt)
    visited = [ False for _ in range(n+1) ]

m = max(cnt_)
for i in range(len(cnt_)):
    if cnt_[i] == m :
        print(i+1, end=" ")