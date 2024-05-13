n = int(input())
num = list(map(int,input().split()))
cnt = [0] * 10
for i in num:
    cnt[i] += 1
for j in cnt[1:]:
    print(j)