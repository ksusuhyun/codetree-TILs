n = int(input())
num = list(map(int,input().split()))
l = [i for i in num if i % 2 == 0]
for j in l:
    print(j, end=' ')