N, M = map(int,input().split())
# 인접 행렬
graph = [ [0 for _ in range(N+1)] for _ in range(N+1) ]
visited = [ False for _ in range(N+1)]

for _ in range(M):
    x, y = map(int,input().split())
    graph[x][y] = 1

def dfs(curr_v):
    for next_v in range(1,N+1):
        if graph[curr_v][next_v] and not visited[next_v]:
            print(next_v)
            visited[next_v] = True
            dfs(next_v)

dfs(1)
# visited[1] = True

# # 인접 리스트
# graph = [ [] for _ in range(N+1) ] # 1~N 번으로 정점 주어짐 => N+1개 만들어야 함
# visited = [ 0 for _ in range(N+1) ]

# for _ in range(M):
#     x,y = map(int,input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# def dfs(vertex):
#     for curr_v in graph[vertex]:
#         if visited[curr_v] == 0:
#             visited[curr_v] = 1
#             dfs(curr_v)

# print()