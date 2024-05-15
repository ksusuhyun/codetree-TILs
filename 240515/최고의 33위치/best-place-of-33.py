n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
max_coin = 0
for i in range(n-2):
    for j in range(n-2):
        coin = 0
        for k in grid[i:i+3][j:j+3]:
            coin += k.count(1)
        max_coin = max(max_coin, coin)
print(max_coin)