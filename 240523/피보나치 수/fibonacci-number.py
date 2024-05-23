n = int(input())

# 1.tabulation
num = [0,1,1]
for i in range(3,n+1):
    num[i] = num[i-1] + num[i-2] 
print(num[n])