score = list(map(int,input().split()))
cnt = [0]*11
for i in score:
    if i != 0:
        cnt[i//10] += 1
    else:
        break
for j in range(10,0,-1):
    print(f'{j*10} - {cnt[j]}')