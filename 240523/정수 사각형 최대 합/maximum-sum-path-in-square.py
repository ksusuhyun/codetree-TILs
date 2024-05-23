n = int(input())
grid = [ list(map(int,input().split())) for _ in range(n) ]
dp = [ [0 for _ in range(n)] for _ in range(n) ]

# 초기화
dp[0][0] = grid[0][0]
# 첫번째 행
for i in range(1,n):
    dp[0][i] = dp[0][i-1] + grid[0][i]
# 첫번째 열
for i in range(1,n):
    dp[i][0] = dp[i-1][0] + grid[i][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = max(dp[i][j-1]+grid[i][j], dp[i-1][j]+grid[i][j])
        
print(dp[n-1][n-1])