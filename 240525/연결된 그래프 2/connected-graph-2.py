n, m = map(int,input().split())
graph = [ [] for _ in range(n+1) ]
for _ in range(m):
    c, n = map(int,input().split())
    graph[c].append(n)
visited = [ False for _ in range(n+1) ]

memo = [ -1 for _ in range(n+1) ]
def dfs(curr):
    if visited[curr]:
        return memo[curr]

    if len(graph[curr]) == 0:
        memo[curr] = 0
        visited[curr] = True
        return memo[curr]

    for next_ in graph[curr]:
        memo[curr] = max(memo[curr],dfs(next_)+1)

    visited[curr] = True
    return memo[curr]

for i in range(1,n+1):
    dfs(i)

maxx = max(memo)
for i in range(len(memo)):
    if memo[i] == maxx:
        print(i, end=" ")