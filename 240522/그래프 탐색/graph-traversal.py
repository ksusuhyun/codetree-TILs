N, M = map(int,input().split())
# 인접 행렬
# graph = [ [0 for _ in range(N+1)] for _ in range(N+1) ]
# visited = [ False for _ in range(N+1)]

# for _ in range(M):
#     x, y = map(int,input().split())
#     graph[x][y] = 1
#     graph[y][x] = 1

# def dfs(curr_v):
#     for next_v in range(1,N+1):
#         if graph[curr_v][next_v] and not visited[next_v]:
#             visited[next_v] = True
#             dfs(next_v)

# dfs(1)
# visited[1] = True
# print(visited.count(True)-1)

# 인접 리스트
graph = [ [] for _ in range(N+1) ] # 1~N 번으로 정점 주어짐 => N+1개 만들어야 함
visited = [ 0 for _ in range(N+1) ]

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(curr_v):
    for next_v in graph[curr_v]:
        if visited[next_v] == 0:
            visited[next_v] = 1
            dfs(next_v)
dfs(1)
visited[1] = 1
print(visited.count(1)-1)