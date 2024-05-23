n = int(input())

# 1.tabulation
# num = [0,1,1]
# for i in range(3,n+1):
#     num.append(num[i-1] + num[i-2])
    
# print(num[n])

# 2.memoization
memo = [-1]*(n+1)
def fibo(n):
    if memo[n] != -1:
        return memo[n]
    if n <= 2:
        memo[n] = 1
        return 1

    memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

fibo(n)
print(memo[-1])