n = int(input())
num = list(map(int,input().split()))
num = sorted(num, reverse=True)
print(num[0],num[1])