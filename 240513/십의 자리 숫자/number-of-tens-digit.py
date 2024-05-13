num = list(map(int,input().split()))
cnt = [0] * 10
for i in num:
    if i != 0:
        cnt[i//10] += 1
    else:
        break
for j in range(1,10):
    print(f'{j} - {cnt[j]}')