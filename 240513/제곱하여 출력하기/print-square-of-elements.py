n = int(input())
num = list(map(int,input().split()))
nums = [i**2 for i in num]
for i in nums:
    print(i, end=' ')