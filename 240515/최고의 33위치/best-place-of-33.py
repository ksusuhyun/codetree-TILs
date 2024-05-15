n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
max_coin = 0
for i in range(n-2): # n-2로 해주는 이유: 3x3 격자가 nxn 격자를 벗어나지 않기 위해
    for j in range(n-2):
        coin = 0
        for m in range(i,i+3):
            coin += grid[m][j:j+3].count(1)
        max_coin = max(max_coin, coin)
print(max_coin)