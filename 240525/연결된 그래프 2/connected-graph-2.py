n, m = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    s,e = map(int,input().split())
    graph[s].append(e)
visited = [ 0 for _ in range(n+1) ]

memo = [ -1 for _ in range(n+1) ]
def dfs(curr):
    if visited[curr] == 2:
        return memo[curr]

    if visited[curr] == 1:
        return memo[curr]

    if len(graph[curr]) == 0:
        memo[curr] = 0
        visited[curr] = 2
        return memo[curr]

    visited[curr] = 1
    memo[curr] = 0

    for next_ in graph[curr]:
        memo[curr] = max(memo[curr],dfs(next_)+1)

    visited[curr] = 2
    return memo[curr]

res = []
for i in range(1,n+1):
    res.append(dfs(i))
    visited = [ 0 for _ in range(n+1) ]
    memo = [ -1 for _ in range(n+1) ]

maxx = max(res)
for i in range(len(res)):
    if res[i] == maxx:
        print(i+1, end=" ")