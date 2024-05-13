num = list(map(int,input().split()))
sum = 0
cnt = 0
for i in num:
    if i != 0:
        sum += i
        cnt += 1
    else:
        break
print(f'{sum} {sum/cnt:.1f}')