num = list(map(int,input().split()))
cnt = [0] * 7
for i in num:
    cnt[i] += 1
for j in range(1,7):
    print(f'{j} - {cnt[j]}')