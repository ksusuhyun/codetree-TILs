n = int(input())
num = list(map(int,input().split()))
dp = [ 0 for _ in range(n) ]
dp[0] = 1
for i in range(1,n):
    for j in range(0,i):
        if dp[j] == 0:
            continue
        if num[j] < num[i]:
            dp[i] = max(dp[j]+1,dp[i])
print(max(dp))