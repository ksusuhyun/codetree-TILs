n = int(input())
num = list(map(int,input().split()))[::-1]
for i in num:
    if i % 2 == 0:
        print(i,end=" ")